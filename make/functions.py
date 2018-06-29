import sys,os
from .filesystem import *


def pathjoin(*args,**kwargs):
	return folder(os.path.join(*args,**kwargs))
