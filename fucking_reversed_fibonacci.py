num = int(input())
fMinusTwo = 0
fMinusOne = 1
f=2
i = 2
while f < num:
    f = fMinusOne + fMinusTwo
    fMinusTwo = fMinusOne
    fMinusOne = f
    rezult = i
    i += 1
if f > num:
    rezult = -1  
if num == 0:
    rezult = 0
if num == 1:
    rezult = 1
print (rezult)
