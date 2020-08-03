n = int(input())
mass = set([i+1 for i in range (n)])
print (mass)
while True:
    quesn= input()
    if quesn == 'HELP':
        break
    elif quesn != 'NO' or quesn !='YES':
        s = set([int(i) for i in quesn.split()])
    elif quesn == 'NO':
        mass = mass - s
    
mass = list(mass)
mass.sort
print (mass)
        
