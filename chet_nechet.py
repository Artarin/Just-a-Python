#Заданы две клетки шахматной доски. Если они покрашены в один цвет, 
#то выведите слово YES, а если в разные цвета — то NO. Программа получает
# на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер 
#строки сначала для первой клетки, потом для второй клетки. 
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a % 2 != 0 and b % 2 !=0:
    perv = 'black'
elif a % 2 == 0 and b %2 ==0:
	perv = 'black'
else:
	perv= 'white'
if c % 2 != 0 and d % 2 !=0:
    vtor = 'black'
elif c % 2 == 0 and d %2 ==0:
	vtor = 'black'
else:
	vtor = 'white'
if perv ==vtor:
	print ('YES')
else:
	print ('NO')
