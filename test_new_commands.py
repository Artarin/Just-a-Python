k=1
n=0
for i in range (1,(int(input())+1)):
    k*=i
    n+=k
    print (i,'',k,'',n)

print (k)