from instructions.Instruction import Instruction

class Line(Instruction):
    """A stand-in line for random lines.
    """

    def __init__(self, n, line):
        super().__init__(n, line)

    def export(self):
        return self.__str__()

    def __str__(self):
        return self.line

    
