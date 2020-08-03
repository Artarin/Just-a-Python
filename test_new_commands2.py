n = int(input())
answer = set([i+1 for i in range (n)])
nonum = set()
while True:
    quesn = input()
    if quesn == 'HELP':
        break
    elif quesn != 'NO' and quesn !='YES':
        s = set([int(i) for i in quesn.split()])
    if quesn =='NO':
        nonum = nonum.update()
    if quesn == 'YES':
        answer = answer.intersection(s)
answer = answer.difference(nonum)
answer = list(answer)
answer.sort
print (' '.join([str(i) for i in answer]))
        
