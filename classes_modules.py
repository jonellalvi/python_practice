class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Group(list):
    def show(self):
        for person in self:
            print person.first_name + " " + person.last_name

g = Group()

p = Person("Kevin", "Long")
print p.first_name

g.append(p)

g.append(Person("Ashley", "Ford"))

k = g[0]
print k.first_name

g.show()
