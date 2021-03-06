#Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. 
# Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел.
#  Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO 
# в противном случае. После нескольких заданныъх вопросов Беатриса запуталась в том,
# какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить,
#  какие числа мог задумать Август.

#В первой строке задано n - максимальное число, которое мог загадать Август.
#  Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом)
#  и ответ Августа на этот вопрос.


#Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.

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
        nonum = nonum.union(s)
    if quesn == 'YES':
        answer = answer.intersection(s)
answer = answer.difference(nonum)
answer = list(answer)
answer.sort
print (' '.join([str(i) for i in answer]))
