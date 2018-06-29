
import os,sys

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

def rule(func=lambda:0):
	o = _rule(func.__name__,func)
	return o



