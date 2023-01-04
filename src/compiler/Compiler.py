import os
import re
import pyperclip

from compiler.Parser import Parser
from compiler.Resolver import Resolver
from compiler.Source import Source
from instructions.Code import Code

class Compiler:
    """The compiler, first called to start the compilation.

    This class will call the parser, then the resolver.
    """

    code = None
    files = []

    parser = None

    def __init__(self):
        self.code = Code()
        self.parser = Parser(self.code)
        #self.preprocessor = Preprocessor()
        for root, dirs, files in os.walk('./src/'):
            for name in files:
                if re.search("\.c$", name):
                    self.files.append(Source(root + "/" + name))

    def compile(self):

        # Preprocessing parsing
        for f in self.files:
            self.code.append(self.parser.parseFile(f))

        Resolver(self.parser).resolve(self.code)
        
    def export(self, filepath):
        code = self.code.export()
        with open(filepath, 'w') as f:
            f.write(code)

        pyperclip.copy(code)

