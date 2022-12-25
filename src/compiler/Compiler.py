import os
import re
from compiler.Preprocessor import Preprocessor

class Compiler:
    """A class description"""
    elements = []
    c = []

    def __init__(self):
        for root, dirs, files in os.walk('./'):
            for name in files:
                if re.search("\.c$", name):
                    self.c.append(root + "/" + name)

    def compile(self):
        for f in self.c:
            self.compileFile(f)
        
    def compileFile(self, filename):
        code = ""
        f = open(filename, "r")
        for line in f:
            m = re.search("^#", line)
            if m:
                if code: 
                    self.elements.append(code)
                    code = ""
                self.elements.append(Preprocessor(line))
            else:
                code = code + line
        self.elements.append(code)

    def resolveIncludes(self):
        for idx, elem in enumerate(self.elements):
            if isinstance(elem, Preprocessor) and elem.action == "include":
                m = re.search("\"(.*)\"", elem.target)
                if m:
                    target = m.group(1)

        
# end ?

