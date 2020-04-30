x='1+1=2'#input()
l=str()
print (x[:x.find('1')])
print (x[x.find('1'):])

for i in range(x.count('1')):
    print (x[:x.find('1')])
    l=(x[:x.find('1')])+'one'+(x[x.find('1')-1:])
    print (l)   

