class Coords:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

c = ['a','b','c','d','e']
for i in range (5):
    c[i] = Coords(int(input()),int(input()))

for i in (c):
    print (id(i),i.__dict__)   

    