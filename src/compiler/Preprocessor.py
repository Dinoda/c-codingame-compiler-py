import re

class Preprocessor:
    
    action = ""
    target = ""

    def __init__(self, line):
        m = re.search("#(\w+) (.*)$", line)
        self.action = m.group(1)
        self.target = m.group(2)

    def __str__(self):
        return "#" + self.action + " " + self.target
