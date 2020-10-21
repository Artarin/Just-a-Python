class Money:
    def __init__(self, d, c):
        self.total_cents = d*100+c
    
    @property
    def dollars (self):
        return self.total_cents // 100

    @property
    def cents (self):
        return self.total_cents % 100

    @dollars.setter
    def dollars(self, value):
        if isinstance (value, int) and value >= 0:
            self.total_cents = value * 100 + self.cents
        else: print ('Error dollars')

    
    @cents.setter
    def cents(self, value):
        if isinstance (value, int) and 100 > value >= 0:
            self.total_cents += value
        else: print ('Error cents')

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents}  центов"

# t = Money (34, 77)

# print (t.__str__())

# t.dollars = 'e'
# t.cents = 33

# print (t.__str__())

user = Money (
    int(input("введите начальное количество долларов на счете ")), 
    int(input("введите начальное число центов на счете  " ))
    )
print (user.__str__())
try:
    k = int(input('Если хотите положить на счет несколько центов, введите их количество:  '))
    if isinstance(k, int):
        user.cents = k
        print (user.__str__())
except:
    print ('ваш счет не изменился')