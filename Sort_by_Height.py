a = [int(i) for i in input().split()]
new_element=int(input())
new_position = 0

while new_position < len(a) and a[new_position] >= new_element:
    new_position+=1
print (new_position+1)
    