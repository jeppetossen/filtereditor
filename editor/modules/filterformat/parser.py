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
        block = "\n\n#" + "="*111 + "\n" + part + "\n" + "#" + "="*111
        return block

    def define_block(self, part):
        block = "\n#" + "-"*36 + "\n" + part + "\n" + "#" + "-"*36
        return block

    def write_section(self, part):
        section = self.define_section(part)
        with open(self.filter, "a") as f:
            f.write(section)

    def find_part(self, i, x=0):
        with open(self.filter, "r") as f:
            part = "0{}0{}".format(i, x)
            for line in f:
                if x == 0 and part in line:
                    return "[[" + part + "]]"
                elif x is not 0 and part in line:
                    return "[" + part + "]"
            f.close()

    def filter_len(self):
        with open(self.filter, "r") as f:
            for i, line in enumerate(f):
                pass
            f.close()
            return i + 1

    def find_content_section(self, part):
        with open(self.filter, "r") as f:
            for i, line in enumerate(f):
                if part in line:
                    return line.replace("\n", "")
            f.close()

    def find_section(self, section):
        sections = self.find_content_section()
        for i in range(len(sections)):
            if sections[i] == section:
                pass
        with open(self.filter, "r") as f:
            for i, line in enumerate(f):
                print(line)
            f.close()

    def find_block(self):
        # block = self.define_block()
        with open(self.filter, "r") as f:
            for i, line in f:
                if line == "#":
                    pass


if __name__ == '__main__':
    obj = Parser("filter.filter")
    # print(obj.find_section("# [[0300]] SHAPER ITEMS"))
    # obj.find_section("# [[0300]] SHAPER ITEMS\n")
    # obj.find_content_section()
    obj.write_section(obj.find_content_section("[[0100]]"))
