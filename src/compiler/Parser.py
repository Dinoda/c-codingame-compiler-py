import re
from instructions.Code import Code
from instructions.Define import Define
from instructions.Ifndef import Ifndef
from instructions.Include import Include
from instructions.Line import Line

class Parser:

    code = None
    stk = []

    def __init__(self, code):
        self.code = code

    def parseFile(self, sourceFile):

        elements = Code(sourceFile)

        with open(sourceFile.name, "r") as f:
            for n, line in enumerate(f):
                m = re.search("^\s*#", line)
                if m:
                    if re.search("\s*#include ", line):
                        elements.append(Include(n+1, line))
                    elif re.search("\s*#define ", line):
                        elements.append(Define(n+1, line))
                    elif re.search("\s*#ifndef", line):
                        ifn = Ifndef(n+1, line, elements.source)
                        elements.append(ifn)
                        self.stack(elements)
                        elements = ifn.statements
                    elif re.search("\s*#endif", line):
                        elements = self.pop()
                else:
                    elements.append(Line(n+1, line))
        return elements

    def stack(self, element):
        self.stk.append(element)

    def pop(self):
        return self.stk.pop()
