#библиотека работает с массивами матрицами


#питоновский список
x = [1,2,3,4,5,6]
print(len(x))
print(type(x))


import numpy as np
#numpy массив
y = np.array([1,2,3,4,5,6])
z = np.array([2,2,2,2,2,2])
#операции + * ** с массивами работают
#два массива также можно умножать

print(y * z)

print(y.sum())
print(y.mean()) #среднее значение
print(y.min())
print(y.max())

#np.random.randint() #случайные целые
#np.random.randn() #для матриц

#d = np.random.randint(1,11, size=5)
#s = np.random.randn(2,3)
#print(s)
#print(s[0,1]) #строка, столбец

#np.random.seed(50) фиксирует результаты и не меняет

r = np.random.randint(1, 100, 5)
print(r)







