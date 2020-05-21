#решение авторов: 
#n = int(input())
#if n == 0:
#    print(0)
#else:
#    a, b = 0, 1
#    for i in range(2, n + 1):
#        a, b = b, a + b
#    print(b)

num = int(input())
fMinusTwo = 0
fMinusOne = 1
for i in range (2,num+1):
    f = fMinusOne+fMinusTwo
    fMinusTwo = fMinusOne
    fMinusOne = f
    
    
if num == 0:
    f = 0
if num == 1:
    f = 1
print (f)
