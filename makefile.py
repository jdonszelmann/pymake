
from make import *

version = '0.0.1'
executable = pathjoin("testdir","build",ARCHITECTURE,version)
for i in CD.dirtree():
	print(i)

# include_folders = 

@rule
def all():
	pass
