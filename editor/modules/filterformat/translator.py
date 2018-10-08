class Translator(object):

    def __init__(self, fname):
        self.filter = fname

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

    def find_table_section(self, part):
        with open(self.filter, "r") as f:
            for i, line in enumerate(f):
                if part in line:
                    break
            f.close()
        return line.replace("\n", "")

    def find_table_block(self, part):
        with open(self.filter, "r") as f:
            for i, line in enumerate(f):
                if part in line:
                    break
            f.close()
        return line.replace("\n", "")

    def find_section(self, section):
        sections = self.find_table_section()
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