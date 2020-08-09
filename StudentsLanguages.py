#Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков. 
# Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.

#В первой строке задано количество школьников. Для каждого из школьников сперва записано количество языков, 
# которое он знает, а затем - названия языков, по одному в строке.

#В первой строке выведите количество языков, которые знают все школьники. 
# Начиная со второй строки - список таких языков. Затем - количество языков,
#  которые знает хотя бы один школьник, на следующих строках - список таких языков.
#  Языки нужно выводить в лексикографическом порядке, по одному на строке.




NumStud = int(input())
ManyLang = set()
stek = set()
EveryStudLang = set()
for i in range (NumStud):  # cycle for students quantity
    NumLang = int(input())
    for j in range (NumLang): # cycle for lang
        stek |= set(input().split())
    if EveryStudLang == {}:
        EveryStudLang |= stek
    EveryStudLang &= stek
    ManyLang |= stek
    stek = set()
list (EveryStudLang)
list (ManyLang)    
print (len(EveryStudLang))
for i in sorted(EveryStudLang):
    print (i)
print (len(ManyLang))
for i in sorted(ManyLang):
    print (i)
