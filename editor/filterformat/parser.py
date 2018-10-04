class Parser(object):

    def __init__(self, file):
        self.filter = file

    def show_hide_found(self):
        showhide = ""
        with open(self.filter, "r") as f:
            for line in f:
                if line == "Show":
                    showhide = "Show"
                elif line == "Hide":
                    showhide = "Hide"
            f.close()
        return showhide

    def define_block(self):
        block = "#=\n#\n#="
        return block

    def define_subblock(self):
        block = "#-\n#\n#-"
        return block

    def find_block(self):
        block = self.define_block()
        with open(self.filter, "r") as f:
            for line in f:
                if line == "#":
                    pass





if __name__ == '__main__':
    obj = Parser("filter.filter")
