n =  int(input())
snow = [0]*n
for i in range (n):
    snow [i] = ['.']*n
for i in range (n):
    for j in range (n):
        if (i + j) == (n-1) or i == j or i == (n//2) or j == (n//2):
            snow[i][j] = '*'
        print (snow[i][j], end =' ')
    print()