import sys


class Command:

    def __init__(self, quiet=False):
        self.quiet = quiet

    def print(self, text, file=sys.stdout, end="\n", force=False):
        if not self.quiet or force:
            print(text, file=file, end=end)

    def print_info(self, text):
        self.print("\x1b[0;32masciinema: %s\x1b[0m" % text)

    def print_warning(self, text):
        self.print("\x1b[0;33masciinema: %s\x1b[0m" % text)

    def print_error(self, text):
        self.print("\x1b[0;31masciinema: %s\x1b[0m" % text, file=sys.stderr, force=True)
