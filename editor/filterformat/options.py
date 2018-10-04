class FilterOptions(object):

    def __init__(self, level):
        self.level = level
        self.filter_level()

    def filter_level(self):
        with open(self.level+".filter", "w") as f:
            f.close()

    def read_block(self):
        pass
