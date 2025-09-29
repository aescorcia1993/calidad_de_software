class CrashGuard:
    def __init__(self, name):
        self.name = name
        self.crashed = False

    def hasCrashedBefore(self):
        return self.crashed

    def markAsCrashed(self):
        self.crashed = True