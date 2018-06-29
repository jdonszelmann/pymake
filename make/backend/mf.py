import os,sys
from .. import _rule

version = 0
if sys.version_info[0] == 2:
	pass
elif sys.version_info[0] == 3 and sys.version_info[1] in [3,4]:
	version = 1
elif sys.version_info[0] == 3:
	version = 2
else:
	raise SystemExit("pymake doesnt work with this version of python")

if version == 0:
	import imp
elif version == 1:
	from importlib.machinery import SourceFileLoader
elif version == 2:
	import importlib.util

def find_makefile():
	for i in os.listdir(os.getcwd()):
		if i.lower().startswith('makefile'):
			return i

def read_makefile(file):
	if version == 0:
		makefile = imp.load_source('makefile', file)
	elif version == 1:
		makefile = SourceFileLoader("makefile", file).load_module()
	elif version == 2:
		spec = importlib.util.spec_from_file_location("makefile", file)
		makefile = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(makefile)
	return {name:rule for name,rule in vars(makefile).items() if type(rule) == _rule}

