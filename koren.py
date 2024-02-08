A = int(input("Введите целое положительное число А: "))
while type(A) != int and A<0:
    try:
        A = int(A)
    except ValueError:
        print("Неверное число!")
        A = input("Введите целое положительное число A: ")
n = int(input("Степень корня n: "))
X = int(input("Введите начальное предположение X: "))
counter = 0
#def koren_chisla():
#    X1 = ((1/n) * ((n-1)*X + A/(pow(X,(n-1)))))
#    return X1
while round(X, 4)!=round(X, 4) or pow(X,n)!=A:    #pow(X,n)!=A:
    
    X1 = ((1/n) * ((n-1)*X + A/(pow(X,(n-1)))))
    X = X1
    if pow(X1,n) == A:
#    if round(X, 4) == round(X1, 4) or pow(X,n)==A:
        break
    counter += 1
    #return X
    #print(X)
print(f"Количество итераций {counter}, искомый корень {round(X,4)}",)
#koren_chisla()