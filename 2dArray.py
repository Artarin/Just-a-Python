Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве. Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.

Программа получает на вход размеры массива n и m, затем n строк по m чисел в каждой. 

n, m = (int(i) for i in  input().split())
tab = []
for i in range (n):
    tab.append ([int(j) for j in input().split()])
elem=tab[0][0]
raw, col = 0, 0
for i in range (len(tab)):
    for j in range (len(tab[i])):
        if tab[i][j] > elem:
            elem = tab[i][j]
            raw, col = i, j
print (raw, col)


Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "." (каждый элемент массива является строкой из одного символа). Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ. В результате единицы в массиве должны образовывать изображение звездочки. Выведите полученный массив на экран, разделяя элементы массива пробелами. 

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

Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке. В левом верхнем углу должна стоять точка. 

s= input()
n = int(s[0])
m = int(s[2])
tab = [['.'] * m for i in range(n)]
for i in range (n):
    for j in range (m):
        if (i + j) % 2 != 0:
            tab[i][j]=('*')
        print (tab[i][j], end=' ')
    print()


Дано число n. Создайте массив размером n×n и заполните его по следующему правилу. На главной диагонали должны быть записаны числа 0. На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д. 

n = int(input())
tab = [[0]*n for i in range (n)]
for raw in range (n):
    for col in range (n):
        tab[raw][col] = abs(raw-col)
        print (tab[raw][col], end = ' ')
    print ()



Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:

Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.

Числа, стоящие выше этой диагонали, равны 0.

Числа, стоящие ниже этой диагонали, равны 2.

Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом. 

n = int(input())
tab = [[0]*n for i in range(n)]

for raw in range (n):
    for col in range (n):
        if (raw + col) == n-1:
            tab[raw][col] = 1
        elif (raw + col) > n-1:
            tab[raw][col] = 2
        print (tab[raw][col], end=' ')
    print()


Дан двумерный массив и два числа: i и j. Поменяйте в массиве столбцы с номерами i и j и выведите результат.

Программа получает на вход размеры массива n и m, затем элементы массива, затем числа i и j.

Решение оформите в виде функции swap_columns(a, i, j). 

def swap_columns(a, i, j):
    for k in range (n):
        a[k][i], a[k][j] = a[k][j], a[k][i]
    return a
#получаем размер массива
n, m =[int(i) for i in input().split()]
tab=[]
# получаем массив построчно
for i in range (n):
    tab.append([int(i) for i in input().split()])
# получаем стобцы, которые поменяем местами
i, j = [int(i) for  i in input().split()]
tab = swap_columns(tab, i, j)
for row in tab:
    print (' '.join([str(elem) for elem in row]))


