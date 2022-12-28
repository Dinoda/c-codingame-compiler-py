class IncludeResolver:

    mainResolver = None
    parser = None

    def __init__(self, parser, main):
        self.parser = parser
        self.mainResolver = main

    def resolve(self, resulting, include):
        if include.local:
            incl = self.parser.parseFile('./src/' + include.target)

            self.mainResolver.resolve(incl)
            resulting.extend(incl)
        else:
            resulting.prepend(include)
