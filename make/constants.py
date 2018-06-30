"""
makefile constants:
"""

import sys,os,platform
from .filesystem import *

#options: nt,posix,?
OS = os.name
#options: Linux, Darwin,Windows
SYSTEM = platform.system()
#options: Vista, 10, 7, 4.15.0-23-generic, etc.
RELEASE = platform.release()
#options: x86_64, i386, etc.
ARCHITECTURE = platform.machine() 
#options: often the same as ARCHITECTURE
CPU = platform.processor()
CD = folder(os.getcwd())


