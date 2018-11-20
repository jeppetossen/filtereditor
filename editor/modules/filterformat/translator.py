class Translator:

    def __init__(self, fname):
        self.filter = fname

    def find_part(self, i, x=0):
        with open(self.filter, "r") as f:
            part = "0{}0{}".format(i, x)
            for line in f:
                if x == 0 and part in line:
                    return "[[{}]]".format(part)
                elif x is not 0 and part in line:
                    return "[{}]".format(part)
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

    def find_table_subsection(self, part):
        with open(self.filter, "r") as f:
            for i, line in enumerate(f):
                if part in line:
                    break
            f.close()
        return line.replace("\n", "")

    def find_section(self, part):
        sections = list()
        section_line = self.find_table_section(part)
        with open(self.filter, "r") as f:
            for i, line in enumerate(f):
                sections.append([i, line])
            f.close()
        section = list()
        for i, line in sections:
            # print(i, section)
            if i - 1 and line == "#" + "="*111:
                section.insert(0, line)
            if line == section_line + "\n":
                section.insert(1, line)
            if i + 1 and line == "#" + "="*111:
                section.insert(2, line)
        del section[-1]
        return section

    def find_subsection(self, part):
        blocks = list()
        block_line = self.find_table_subsection(part)
        with open(self.filter, "r") as f:
            for i, line in enumerate(f):
                blocks.append([i, line])
            f.close()
        block = list()
        for i, line in blocks:
            if i - 1 and line == "#":
                pass
            if line == block_line + "\n":
                pass
            if i + 1 and line == "#":
                pass
        del block[-1]
        return block

    def find_showhide(self):
        with open(self.filter, "r") as f:
            for i, line in enumerate(f):
                if line == "Show":
                    pass
                elif line == "Hide":
                    pass
                else:
                    return None
                return line


if __name__ == '__main__':
    obj = Translator("filter.filter")
    # obj.find_section("# [[0100]] OVERRIDE AREA 1 - Override ALL rules here")
    obj.find_section("0100")
    # print(obj.find_table_section("0100"))
