num1 = int(input())
num2 = int(input())
i = 1
k = 1
while num2 != 0 :
    
    #if num2 == 0:
     #   break
    if num1 == num2:
        i += 1  
        print (i)          
    else:
        if k < i:
            k = i
        i = 1
    num1, num2 = num2, num1
    num2 = int(input())
 #   num1 = int(input())
print (k)