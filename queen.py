#Шахматный ферзь ходит по диагонали, горизонтали или вертикали. Даны две
# различные клетки шахматной доски, определите, может ли ферзь попасть с
# первой клетки на вторую одним ходом. 
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if abs (x-x1) == abs(y-y1):
	print ('YES')
elif (x==x1) or (y==y1):
	print ('YES')
else:
	print ('NO')