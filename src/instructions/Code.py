class Code:
    """A code element, containing a set of instructions

    This class is used to contain a set of instructions, this
    is at the same time the basis (root) of the whole program
    and a part of it.
    """

    # The source file of the code, can be None for the root
    source = None

    # The instruction list of the code
    code = []

    def __init__(self, source=None):
        self.source = source
        self.code = []

    def append(self, code):
        self.code.append(code)

    def extend(self, code):
        self.code.extend(code.code)

    def remove(self, code):
        self.code.remove(code)

    def prepend(self, code):
        self.code.insert(0, code)

    def detail(self): 
        det = ""
        for x in self.code:
            det = det + x.__str__()
        return det

    def debug(self):
        for x in code:
            x.debug()

    def export(self):
        exp = ""
        for x in self.code:
            if x != None:
                exp = exp + x.export()
        return exp

    def __str__(self):
        return self.detail()
