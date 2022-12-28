class Source:
    """The source class, connected to a source file

    This class is used to connect a code line to a source.
    """

    name = None

    def __init__(self, filename):
        self.name = filename

