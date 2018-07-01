import sys,os,shutil

import ctypes
def is_hidden(filepath):
    name = os.path.basename(os.path.abspath(filepath))
    return name.startswith('.') or has_hidden_attribute(filepath)

def has_hidden_attribute(filepath):
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(unicode(filepath))
        assert attrs != -1
        result = bool(attrs & 2)
    except (AttributeError, AssertionError):
        result = False
    return result

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

class folder:
	def __init__(self,path=os.getcwd()):
		if not os.path.exists(os.path.dirname(path)):
			from .backend import argparser
			if not argparser.parse_args(sys.argv).yes:
				print("{} does not yet exist. do you want to make it? [Y/n]".format(path))
				res = input(">>>").lower()
				if "y" not in res:
					raise SystemExit("couldn't continue due to non-existing folder")
			os.makedirs(os.path.dirname(path))
		self.path = path

	def __iter__(self):
		if os.path.isdir(self.path):
			for i in listdir_fullpath(self.path):
				yield folder(i)
		else:
			yield self

	def tree(self):
		if os.path.isdir(self.path) and not is_hidden(self.path):
			for i in self:
				if not is_hidden(i.path) and not i.path.startswith("."):
					yield i
				yield from i.tree()

	def filetree(self):
		if os.path.isdir(self.path) and not is_hidden(self.path):
			for i in self:
				if os.path.isfile(i.path):
					if not is_hidden(i.path) and not i.path.startswith("."):
						yield i
				yield from i.filetree()

	def dirtree(self):
		if os.path.isdir(self.path) and not is_hidden(self.path):
			for i in self:
				if os.path.isdir(i.path):
					if not is_hidden(i.path) and not i.path.startswith("."):
						yield i
				yield from i.dirtree()

	@property				
	def name(self):
		return os.path.basename(self.path)

	def __repr__(self):
		return self.path

	def __str__(self):
		return self.path

	def __getattr__(self,attr):
		if os.path.isdir(self.path) and attr in os.listdir(self.path):
			return folder(os.path.join(self.path,attr))

		try:
			return super().__getattribute__(attr)
		except AttributeError:
			raise
			# from .backend import argparser
			# if not argparser.parse_args(sys.argv).yes:
			# 	print("{} does not yet exist. do you want to make it? [Y/n]".format(os.path.join(self.path,attr)))
			# 	res = input(">>>").lower()
			# 	if "y" not in res:
			# 		raise SystemExit("couldn't continue due to non-existing folder")
			# os.makedirs(os.path.join(self.path,attr))			
			# return folder(os.path.join(self.path,attr))

	def __getitem__(self,item):
		if os.path.isdir(self.path) and item in os.listdir(self.path):
			return folder(os.path.join(self.path,item))


	def print(self):
		print(self)

	def printtree(self,indent=0):
		if os.path.isdir(self.path) and not is_hidden(self.path) and not self.path.startswith(".") and not self.path.startswith("_"):
			for i,j in zip(os.listdir(self.path),self):
				if not is_hidden(j.path) and not j.path.startswith("."):
					print(" "*indent,end="")
					print(i)
				j.printtree(indent+1)

	def get(self,mode="r"):
		if os.path.isfile(self.path):
			return open(self.path,mode)

	def remove(self):
		shutil.rmtree(self.path)

	def removechildren(self):
		for i in listdir_fullpath(self.path):
			shutil.rmtree(i)