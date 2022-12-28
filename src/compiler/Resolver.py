from instructions.Include import Include
from instructions.Ifndef import Ifndef
from IncludeResolver import IncludeResolver
from instructions.Define import Define

class Resolver:

    parser = None
    values = {}

    def __init__(self, parser):
        self.parser = parser
        self.values = []
        self.includeR = IncludeResolver(parser, self)

    def resolve(self, code):
        res = Code()
        for x in code.code:
            if isinstance(x, Include):
                ret = self.includeR.resolve(res, x)
            elif isinstance(x, Define):
                self.values[x.name] = x.value
            elif isinstance(x, Ifndef):
                if x.condition not in self.values:


