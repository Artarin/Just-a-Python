#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать 
# маршрут длиной m километров? Программа получает на вход числа n и m. 
n=int(input())
m=int(input())
import math
print (math.ceil(m/n))