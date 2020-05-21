n = 8 # int(input())
fMinusTwo = 0
fMinusOne = 1
for i in range (2,n):
    f = fMinusOne+fMinusTwo
    fMinusTwo = fMinusOne
    fMinusOne = f
    print (f)
    
if n == 0:
    num = 0
if n == 1:
    num = 1
print (num)

k=1
l=0
while k!=0:
    if l<i:
       l=i
    k=i
    i=int(input())
print (l)