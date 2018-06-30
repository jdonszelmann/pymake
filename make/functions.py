import sys,os,re,inspect,collections
from .filesystem import *


def pathjoin(*args):
	args = [i if type(i) != folder else i.path for i in args ]
	return folder(os.path.join(*args))

def createfolders(*args):
	for i in args:
		if isinstance(i, collections.Iterable) and type(i) != str:
			createfolders(*i)
			continue
		if not os.path.exists(os.path.dirname(i)):
			os.makedirs(os.path.dirname(i))

def combine(*args):
	for i in args:
		for j in i:
			yield j

def match(iterable,pattern):
	# for i in iterable:
	# 	print(pattern,str(i),re.match(pattern,str(i)))

	return list(filter(lambda i:re.search(pattern,str(i))!=None,iterable))

def sub(iterable,pattern1,pattern2):
	return list(map(lambda i:re.sub(pattern1,pattern2,str(i)),iterable))


def format_type(t):
	if type(t) in [int,str,float,bool]:
		return str(t)
	elif type(t) in [list,tuple]:
		return " ".join(t)
	elif type(t) in [Ellipsis,None]:
		return ""
	else:
		return repr(t)	

def format_command(command,scope):
	res = re.split(r"(\$\(.*?\))",command)
	for index,i in enumerate(res):
		g = re.match(r"\$\((.*?)\)",i)
		if g:
			var = g.group(1)
			if var not in scope:
				raise ValueError("{} is not a variable or could not be found".format(var))
			res[index]=format_type(scope[var])
	command = "".join(res)
	res = re.split(r"(\@\(.*?\)\@)",command)
	for index,i in enumerate(res):
		g = re.match(r"\@\((.*?)\)\@",i)
		if g:
			code = g.group(1)
			res[index]=format_type(eval(code,scope))
	return res

def shell(command,scope=None):
	if scope == None: 
		scope = inspect.currentframe().f_back.f_globals
		scope.update(inspect.currentframe().f_back.f_locals)
	res = format_command(command,scope)
	os.system("".join(res))

def shellecho(command,scope=None):
	if scope == None: 
		scope = inspect.currentframe().f_back.f_globals
		scope.update(inspect.currentframe().f_back.f_locals)
	res = format_command(command,scope)
	print("".join(res))
	os.system("".join(res))

def echo(command,scope=None):
	if scope == None: 
		scope = inspect.currentframe().f_back.f_globals
		scope.update(inspect.currentframe().f_back.f_locals)
	res = format_command(command,scope)
	os.system("echo " + "".join(res))

def apply(function,*iterables):
	for i in zip(*iterables):
		function(*i)

def require(*args):
	def retfunc(src=None,dest=None):
		for i in args:
			i.convert(src,dest)
	return retfunc