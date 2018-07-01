
from make import *

version = '0.0.1'
builddir = pathjoin("testdir","build")
executable = pathjoin(builddir,ARCHITECTURE,version)


include_folders = match(CD.testdir.src.dirtree(),r"include")
asm_src = match(CD.testdir.src.filetree(),r".*\.asm$")
c_src = match(CD.testdir.src.filetree(),r".*\.c$")
cpp_src = match(CD.testdir.src.filetree(),r".*\.cpp$")

asm_o = sub(asm_src,r"src/(.*)\.asm",r"build/\1.o")
c_o = sub(c_src,r"src/(.*)\.c",r"build/\1.o")
cpp_o = sub(cpp_src,r"src/(.*)\.cpp",r"build/\1.o")

createfolders(asm_o,c_o,cpp_o)

asm_flags = ["-felf32"] + ["-I{}".format(i) for i in include_folders]
c_flags = ['-Wall','-cpp','-O3','-g'] + ["-I{}".format(i) for i in include_folders]
cpp_flags = ['-Wall','-cpp','-O3','-g','--std=c++11'] + ["-I{}".format(i) for i in include_folders]
ldflags = ""

linker = "gcc"

@converter(c_src,c_o)
def CtoO(source,dest):
	echo("c: compiling @(source.name)@")
	shell("gcc $(c_flags) -c $(source) -o $(dest)")

@converter(cpp_src,cpp_o)
def CPPtoO(source,dest):
	echo("cpp: compiling @(source.name)@")
	shell("g++ $(c_flags) -c $(source) -o $(dest)")

@converter(asm_src,asm_o)
def ASMtoO(source,dest):
	echo("asm: compiling @(source.name)@")
	shell("nasm $(c_flags) -c $(source) -o $(dest)")

compile = require(CtoO,CPPtoO,ASMtoO)

def link():
	echo("linking...")
	shell("$(linker) $(ldflags) -o $(executable) @(list(combine(asm_o,c_o,cpp_o)))@")

@rule
def install():
	shell("sudo apt-get install libboost-all-dev -y")
	shell("sudo apt-get install aptitude -y")
	shell("aptitude search boost")
	shell("sudo apt-get install nasm gcc valgrind gdb -y")

@rule
def all():
	compile()
	link()

@rule
def run():
	all()
	shell("$(executable) /home/jonathan/Documents/foxlang/test.fox")

@rule
def clean():
	builddir.removechildren()