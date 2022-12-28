import re
from instructions.Code import Code
from instructions.Define import Define
from instructions.Ifndef import Ifndef
from instructions.Include import Include

class Parser:

    code = None
    stack = []

    def __init__(self, code):
        self.code = code

    def parseFile(self, sourceFile):

        elements = Code()
        codePart = CodePart()

        f = open(sourceFile.name, "r")

        for line in f:
            m = re.search("^\s*#", line)
            if m:
                if not codePart.empty:
                    elements.append(codePart)
                    codePart = CodePart()
                if re.search("\s*#include ", line):
                    elements.append(Include(line))
                elif re.search("\s*#define ", line):
                    elements.append(Define(line))
                elif re.search("\s*#ifndef", line):
                    ifn = Ifndef(line)
                    elements.append(Ifndef(line))
                    self.stack(elements)
                    elements = ifn
                elif re.search("\s*#endif", line):
                    elements = self.pop()
            else:
                codePart.append(line)
        elements.append(codePart)
        return elements

    def stack(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()
