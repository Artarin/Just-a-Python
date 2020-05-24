num1 = -1
num2 = int(input())
i = 1
k = 1
while num2 != 0 :
    if num1 == num2:
        i += 1 
        k = max(k, i)
    else:
        i=1 
    num1, num2 = num2, num1
    num2 = int(input())
print (k)

#решение разработчиков:
#prev = -1
#curr_rep_len = 0
#max_rep_len = 0
#element = int(input())
#while element != 0:
#    if prev == element:
#        curr_rep_len += 1
#    else:
#        prev = element
#        max_rep_len = max(max_rep_len, curr_rep_len)
#        curr_rep_len = 1
#    element = int(input())
#max_rep_len = max(max_rep_len, curr_rep_len)
#print(max_rep_len)

