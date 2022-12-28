import re
from instructions.Instruction import Instruction
from instructions.Code import Code

class Ifndef(Instruction):
    """A preprocessor instruction: #ifndef

    This is used to define its content if the given 
    condition is not defined by a #define instruction.
    """

    # Statements, inserted in a Code element
    statements = None
    # The condition (if it is defined, the statements are not executed)
    condition = ""

    def __init__(self, n, line):
        super().__init__(n, line)

        self.statements = Code()

        m = re.search('#ifndef (.*)', line)
        self.condition = m.group(1)

        if not self.condition:
            self.error("A condition is mandatory for a \"ifndef\" instruction")

    def __str__(self):
        ret = "#ifndef " + self.condition + "\n"

        for x in self.statements:
            ret = ret + x + "\n"

        return ret + "#endif\n"

