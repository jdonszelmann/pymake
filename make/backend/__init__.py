from .argparser import *
from .mf import *


def make(filename=find_makefile(),*rules):
	file = read_makefile(filename)
	for i in rules:
		if i not in file:
			raise SystemExit("no rule with name {}".format(i))
		else:
			file[i].run()

def makeargs(args):
	file = args.file
	rules = [args.rules] if type(args.rules) != list else args.rules
	make(file,*rules)

