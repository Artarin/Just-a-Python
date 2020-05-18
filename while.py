#найти наименьший натур делитель больше 1. решение авторов num%i!=0

num=int(input())
i=2
while num/i!=num//i:
    i+=1
print (i)