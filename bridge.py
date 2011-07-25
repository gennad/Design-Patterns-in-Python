class AbstractParser:
    def __init__(self, scanner):
        self.scanner = scanner

class ExprParser(AbstractParser):
    def expr(self):
        t = self.scanner.next()...
        self.scanner.push_back(t)...

