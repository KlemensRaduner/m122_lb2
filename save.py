class Save:
    def __init__(self, dir, extensions):
        self.dir = dir
        self.extensions = extensions

    def hasExtension(self, e):
        return e in self.extensions
