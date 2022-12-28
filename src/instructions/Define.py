import re
from instructions.Instruction import Instruction

class Define(Instruction):
    """A preprocessor instruction: #define

    This is used to define a new value in the preprocess, which
    is the part that is of interest in what we are doing.
    """

    # The name of the element to define
    name = ""
    # The value to define the element to (not mandatory)
    value = None

    def __init__(self, n, line):
        super().__init__(n, line)

        m = re.search('#define (.*)\s+?(.*)?', line)
        self.name = m.group(1)
        if m.group(2):
            self.value = m.group(2)
        if not self.name:
            self.error("No name for \"define\" instruction is not authorized")

    def __str__(self):
        s = "#define " + self.name
        if self.value:
            s = s + ' ' + self.value
        return s
