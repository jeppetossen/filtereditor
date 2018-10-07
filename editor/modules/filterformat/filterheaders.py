from editor.modules.content.headers import fetch_header


class FilterHeaders:

    def __init__(self):
        self.headers_raw = fetch_header()

    def block_translator(self):
        _indent = "    "
        _disabledLine = "#"
        _newLine = "\n" + _indent

