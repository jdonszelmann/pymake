# import sys,os,re

# from .filesystem import *
# from .constants import *
# from .functions import *

# #defaults for compiling

# class compilers:
# 	data = {
# 		"c":[
# 				(r".*\.c$","gcc",["-Wall",'-cpp','-O3'],True),
# 				(r".*\.c$","clang",["-Wall",'-cpp','-O3','-fPIC'],True),
# 			],
# 		"cpp":[
# 				(r".*\.cpp$","g++",['-Wall','-cpp','-O3','--std=c++11'],True),
# 				(r".*\.cpp$","clang",['-Wall','-cpp','-O3','--std=c++11','-fPIC'],True),
# 			],
# 		"nasm":[
# 				(r".*\.asm$","nasm",["-felf32"],True),
# 			],
# 		"python":[
# 				(r".*\.py$",None,None,False),
# 			]
# 	}

# 	@classmethod
# 	def setpattern(cls,name,command,pattern):
# 		cls.data[name][0] = pattern

# 	@classmethod
# 	def getpattern(cls,command,name):
# 		return cls.data[name][0]

# 	@classmethod
# 	def appendflags(cls,name,command,*flags):
# 		if type(flags[0]) == list:
# 			flags = flags[0]
# 		cls.data[name][2] += flags

# 	@classmethod
# 	def setflags(cls,name,command,*flags):
# 		if type(flags[0]) == list:
# 			flags = flags[0]
# 		cls.data[name][2] = flags

# 	@classmethod
# 	def getflags(cls,command,name):
# 		return cls.data[name][2]

# 	@classmethod
# 	def setcompiler(cls,name,command,compiler):
# 		cls.data[name][1] = compiler

# 	@classmethod
# 	def getcompiler(cls,name,command):
# 		return cls.data[name][1]

# 	@classmethod
# 	def setinclude(cls,name,command,value):
# 		cls.data[name][3] = value

# 	@classmethod
# 	def getinclude(cls,command,name):
# 		return cls.data[name][3]

# 	@classmethod
# 	def getlang(cls,name):
# 		return cls.data[name]

# 	@classmethod
# 	def get(cls,file):
# 		for lang,value in cls.data.items():
# 			for option in value:
# 				if re.match(option[0],str(file)):
# 					yield option

# def trycompile(src,dest,flags,compiler):
# 	try:
# 		shell("$(compiler) $(flags) -c $(src) -o $(dest)")
# 		return 1
# 	except CommandNotFoundError:
# 		return 0


# def autocompile(src,dest,include=[]):
# 	if type(include) == str:
# 		include = match(CD.dirtree(),include)
# 	includes = ["-I{}".format(i) for i in include]

# 	if type(src) != list:
# 		src = [src]

# 	if type(dest) != list:
# 		dest = [dest]

# 	for i,j in zip(src,dest):
# 		for x in compilers.get(i):
# 			if x[1] == None:
# 				continue
# 			if x[3]:
# 				flags = x[2] + includes
# 				if trycompile(i,j,flags,x[1]):
# 					break
