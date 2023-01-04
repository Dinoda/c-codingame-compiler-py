import os
import re
from instructions.Include import Include
from instructions.Ifndef import Ifndef
from instructions.Define import Define
from instructions.Code import Code
from compiler.Source import Source

class Resolver:

    parser = None
    values = {}
    external_include = []

    def __init__(self, parser):
        self.parser = parser
        self.values = {}

    def resolve(self, code):
        for idx, x in enumerate(code.code):
            if isinstance(x, Code):
                self.resolve(x)
            elif isinstance(x, Include):
                target = x.target
                if x.local:
                    direct = os.path.dirname('src/')
                    if code.source:
                        direct = os.path.dirname(os.path.realpath(code.source.name))
                        while re.search('^\.\./', target):
                            direct = os.path.dirname(os.path.realpath(direct))
                            target = re.sub('^\.\./', '', target)
                    s = Source(direct + "/" + x.target.replace("../", ""))
                    x.including(self.parser.parseFile(s))
                    self.resolve(x.code)
                else:
                    if x.target in self.external_include:
                        code.code[idx] = Code()
                    else:
                        self.external_include.append(x.target)
            elif isinstance(x, Define):
                self.values[x.name] = x.value
            elif isinstance(x, Ifndef):
                if x.condition not in self.values:
                    self.resolve(x.statements)
                else:
                    code.code[idx] = Code()

