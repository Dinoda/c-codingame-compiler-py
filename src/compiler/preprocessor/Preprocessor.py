from instructions.Preprocessor import Preprocessor as PreprocessorInstruction

class Preprocessor:

    code = None
    stack = []
    state = None

    def preprocess(self, code):
        self.code = code
        for idx, elem in enumerate(elements):
            if isinstance(elem, PreprocessorInstruction):
                match elem.action:
                    case "include":
                        self.include(elem)

    def include(self, element):
        m = re.search("\"(.*)\"", element.target)
        if m:
            f = m.group(1)
        else:
            

