import re
from instructions.Instruction import Instruction

class Include(Instruction):
    """A preprocessor instruction: #include

    Used to include another file or code in the 
    software.
    """
    
    local = False
    target = ""
    code = None

    def __init__(self, n, line):
        super().__init__(n, line)

        m = re.search('#include <(.*)>', line)
        if m:
            self.target = m.group(1)
        else:
            m = re.search('#include "(.*)"', line)
            self.local = True
            self.target = m.group(1)

        self.code = None

        if not self.target:
            self.error('A target is mandatory for "include" instruction')

    def including(self, code):
        self.code = code

    def export(self):
        if self.code:
            return self.code.export()
        elif not self.local:
            return "#include <" + self.target + ">\n"
        return ""

    def __str__(self):
        if self.code:
            return self.code.__str__()
        s = "#include "
        if self.local:
            s = s + '"' + self.target + '"\n'
        else:
            s = s + "<" + self.target + ">\n"
        return s
