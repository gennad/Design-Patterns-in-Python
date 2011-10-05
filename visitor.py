class CodeGeneratorVisitor(object):
    @dispatch.on('node')
    def visit(self, node):
        """This is the generic method"""

    @visit.when(ASTNode)
    def visit(self, node):
        map(self.visit, node.children)

    @visit.when(EchoStatement)
    def visit(self, node):
        self.visit(node.children)
        print "print"

    @visit.when(BinaryExpression)
    def visit(self, node):
        map(self.visit, node.children)
        print node.props['operator']

    @visit.when(Constant)
    def visit(self, node):
        print "push %d" % node.props['value']

sometree = None
CodeGeneratorVisitor().visit(sometree)
# Output:
# push 1
# print
# push 2
# push 4
# push 3
# multiply
# plus
# print
