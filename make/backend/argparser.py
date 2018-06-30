

from .mf import find_makefile
import argparse


def create_parser():
	p = argparse.ArgumentParser(description="Build and compile any program with pymake")
	p.add_argument('fname', type=str, nargs=1,help=argparse.SUPPRESS)
	p.add_argument('rules', metavar='rules', type=str, nargs='*',default="all", help='which rules to run')
	p.add_argument("-f","--file",help="makefile location",default=find_makefile())
	p.add_argument("-y","--yes",help="yes to all questions",action="store_true")
	p.add_argument("-p","--params",nargs='*')
	# p.add_argument("-r","--recompile",help="recompiles every file",action="store_true")
	return p

def parse_args(args):
	parser = create_parser()
	return parser.parse_args(args)

if __name__ == '__main__':
	parse_args(sys.argv)