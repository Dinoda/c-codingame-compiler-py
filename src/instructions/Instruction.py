class Instruction:
    """An instruction superclass

    This is used to keep the line and line number of 
    the instruction.
    """

    n = -1
    line = None

    def __init__(self, n, line):
        self.n = n
        self.line = line

    def error(self, desc):
        print("Error line " + self.n + ": \"" + self.line + "\"\n")
        print("\t\t" + desc)

