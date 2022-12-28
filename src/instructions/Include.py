import re

class Include:
    """A preprocessor instruction: #include

    Used to include another file or code in the 
    software.
    """
    
    local = False
    target = ""

    def __init__(self, n, line):
        super().__init__(n, line)

        m = re.search('#include <(.*)>', line)
        if m:
            self.target = m.group(1)
        else:
            m = re.search('#include "(.*)"', line)
            self.local = True
            self.target = m.group(1)
        if not self.target:
            self.error('A target is mandatory for "include" instruction')

    def __str__(self):
        s = "#include "
        if self.local:
            s = s + '"' + self.target + '"'
        else:
            s = s + "<" + self.target + ">"
        return s
