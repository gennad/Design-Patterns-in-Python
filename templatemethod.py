class AbsBase(object):
    def orgMethod(self):
        self.dothis()
        self.dothat()
class Concrete(AbsBase):
    def dothis(self): ...

class AbsPager(object):
    def __init__(self,mx=60):
        self.cur = self.pg = 0
        self.mx = mx
    def writeline(self,line):
        """organizing method"""
    def writeline(self,line):
        if self.cur == 0:
        self.dohead(self.pg)
    self.dowrite(line)
    self.cur += 1
    if self.cur>=self.mx:
        self.dofoot(self.pg)
        self.cur = 0
        self.pg += 1

class Pagerout(AbsPager):
    def dowrite(self,line):
        print line
    def dohead(self,pg):
        print 'Page %d:\n' % pg+1
    def dofoot(self,pg):
        print '\f',

class Cursepager(AbsPager):
    def dowrite(self,line):
        w.addstr(self.cur,0,line)
    def dohead(self,pg):
        w.move(0,0); w.clrtobot()
    def dofoot(self,pg):
        w.getch() # wait for key
