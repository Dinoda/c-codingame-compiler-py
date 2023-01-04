import os
import sys

from compiler.Compiler import Compiler
from compiler.Parser import Parser

print("Compiling for Codingame")

f = Compiler()

f.compile()

f.export(sys.argv[1])
