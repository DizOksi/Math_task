import math

A = int(input("Введите одно из значений угла А'(60,90,120): "))
c = int(input("Введите значение стороны c' треугольника: "))
h = int(input("Введите значение высоты треугольника: "))
#a = print("a =", h*2)
a = int(h*2)
#print("b =", int(c))
b = int(c)
p = ((a + b + c)/2)
print("a =", a)
print("b =", int(c))
print("Полупириметр p =", int(p))
a = int(a)
conv_grad = math.radians(A/2)
R = (p-a) * math.tan(conv_grad)
S = math.pi * math.pow(R,2)
print("S =", S)

# def right_triangle(*l):
#     a, b, c = sorted(l)
#     return a > 0 and a * a + b * b == c * c
# a, b, c = map(float,input().split())
# a, b, c = sorted([a,b,c])
# if a*a+b*b == c*c:
#    print('OK')
# else:
#    print("NOT")