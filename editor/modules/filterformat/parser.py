from .translator import Translator


class Parser:

    def __init__(self, fname):
        self.filter = fname
        self.translator = Translator(fname)

    def define_section(self, part):
        block = "\n\n#" + "="*111 + "\n" + part + "\n" + "#" + "="*111
        return block

    def define_block(self, part):
        block = "\n\n#" + "-"*36 + "\n" + part + "\n" + "#" + "-"*36
        return block

    def write_section(self, part):
        area = self.translator.find_table_section(part)
        section = self.define_section(area)
        with open(self.filter, "a") as f:
            f.write(section)
            f.close()

    def write_block(self, part):
        area = self.translator.find_table_block(part)
        block = self.define_block(area)
        with open(self.filter, "a") as f:
            f.write(block)
            f.close()

    def write_condition(self, part):
        pass


if __name__ == '__main__':
    obj = Parser("filter.filter")
    # print(obj.find_section("# [[0300]] SHAPER ITEMS"))
    # obj.find_section("# [[0300]] SHAPER ITEMS\n")
    # obj.find_content_section()
    obj.write_section("0100")
    # obj.write_block("0301")
