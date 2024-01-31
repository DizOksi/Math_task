A = int(input("Введите целое положительное число А: "))
n = int(input("Степень корня n: "))
X = int(input("Введите начальное предположение X: "))
#def koren_chisla():
#    global X
#    X = ((1/n) * ((n-1)*X + A/(pow(X,(n-1)))))
#    return X
while pow(X,n)!=A:
    X = ((1/n) * ((n-1)*X + A/(pow(X,(n-1)))))
        
    if pow(X,n) == A:
        break
#    return X
    print(X)
#koren_chisla()