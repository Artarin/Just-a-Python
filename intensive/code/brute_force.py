class Person:

    def __init__(self, name):
        self.name = name
    def breath(self):
        print('breath')
    name = 'adam'
    def walk(self):
        print ('walk')

class Doctor(Person): #subclass
    def breath(self):
        print ('fuck off')
    name = 'fil'


d = Doctor('doc')
p = Person('pers')

d.breath()
p.breath()
print (d.name, p.name)
print (d,p)