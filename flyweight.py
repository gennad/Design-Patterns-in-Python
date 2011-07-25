"""
Flyweight Design Pattern
   Desc: Sharing the shareable data between the common classes and thus reducing the memory usage
   Code: Believing that every person in a family will have same genetic structure, we will create a code to learn about
         genetics of each family. If a same member of a family is given, no new object is created. (You can also create new
         objects unlike here but keep a reference of the heavy weighted one in the new |||r object).
"""

class ComplexGenetics(object):
    """ returns a huge genetic pattern"""
    def __init__(self):
        pass

    def genes(self, gene_code):
        return "ComplexPatter[%s]TooHugeinSize" % (gene_code)

class Families(object):
    """ To learn about Family Genetic Pattern """
    family = {}
    def __new__(cls, name, family_id):
        """ i have to capture the details before the class is created, __init__ is pseudo constructor """
        try:
            id = cls.family[family_id]
        except KeyError:
            id = object.__new__(cls)
            cls.family[family_id] = id
        return id

    def set_genetic_info(self, genetic_info):
        cg = ComplexGenetics()
        self.genetic_info = cg.genes(genetic_info)

    def get_genetic_info(self):
        return (self.genetic_info)

def test():
     # name, family_id and genetic code details (i dont care if genetic code detail varies in same family [it is research fault :-D ])
    data = (('a', 1, 'ATAG'), ('a', 2, 'AAGT'), ('b', 1, 'ATAG'))
    family_objects = []
    for i in data:
        obj = Families(i[0], i[1])
        obj.set_genetic_info(i[2])
        family_objects.append(obj)

    for i in family_objects:
        print "id = " + str(id(i))
        print i.get_genetic_info()
    print "similar id's says that they are same objects "

if __name__ == '__main__':
    test()
