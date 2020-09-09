dict = {}
for _ in range (int(input())): # input number of strings
    for i in input().split(): 
        dict[i] = dict.get(i, 0) + 1
#print (dict)

#List = sorted([(k,i)for i, k in dict.items()])
List = sorted((tuple(reversed(i)) for i in dict.items()), reverse = True)
#for i in range(len(List)):
#    print (List[i][1])
print(List)


# https://pythontutor.ru/lessons/dicts/problems/frequency_analysis/