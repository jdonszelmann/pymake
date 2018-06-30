
import os,sys,inspect

from .filesystem import *
from .constants import *
from .functions import *

class _rule(object):
	def __init__(self,name,func):
		self.name = name
		self.function = func

	def run(self):
		self.function()

	def __repr__(self):
		return "rule {self.name}".format(self=self)

	def __call__(self,*args,**kwargs):
		self.function(*args,**kwargs)


def requires(requirement):
	def retfunc(func):
		print(func)
	return retfunc

def rule(func):
	o = _rule(func.__name__,func)
	return o


class _converter:
	def __init__(self,func,src=None,dest=None):
		self.src = src
		self.dest = dest
		self.func = func

	def convert(self,src=None,dest=None):
		if src == None:
			if self.src != None:
				src = self.src
			else:
				raise ValueError("couldn't determine source")
		if dest == None:
			if self.dest != None:
				dest = self.dest
			else:
				raise ValueError("couldn't determine destination")
		for i,j in zip(src,dest):
			self.func(i,j)

def converter(source=None,dest=None):
	def retfunc(func):
		return _converter(func,source,dest)
	if inspect.isfunction(source):
		return retfunc(source)
	return retfunc