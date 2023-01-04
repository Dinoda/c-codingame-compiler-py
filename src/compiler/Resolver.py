import os
from instructions.Include import Include
from instructions.Ifndef import Ifndef
from instructions.Define import Define
from instructions.Code import Code
from compiler.Source import Source

class Resolver:

    parser = None
    values = {}

    def __init__(self, parser):
        self.parser = parser
        self.values = {}

    def resolve(self, code):
        for x in code.code:
            if isinstance(x, Code):
                self.resolve(x)
            elif isinstance(x, Include):
                if x.local:
                    direct = os.path.dirname('src/')
                    if code.source:
                        direct = os.path.dirname(os.path.realpath(code.source.name))
                    s = Source(direct + "/" + x.target)
                    x.including(self.parser.parseFile(s))
                    self.resolve(x.code)
            elif isinstance(x, Define):
                self.values[x.name] = x.value
            elif isinstance(x, Ifndef):
                if x.condition not in self.values:
                    self.resolve(x.statements)

