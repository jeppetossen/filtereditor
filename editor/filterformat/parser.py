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

    def define_section(self, part):
        block = "#" + "="*111 + "\n" + "# " + part + "\n" + "#" + "="*111
        return block

    def define_block(self, part):
        block = "#" + "-"*36 + "\n" + "# " + part + "\n" + "#" + "-"*36
        return block

    def find_section(self):
        section = self.define_section()
        with open(self.filter, "r") as f:
            for line in f:
                if line == "#":
                    pass

    def find_block(self):
        block = self.define_block()
        with open(self.filter, "r") as f:
            for line in f:
                if line == "#":
                    pass
