'''Задание 1'''
n_1 = 8
n_2 = 4

print(n_1 + n_2)
print(n_1 - n_2)
print(n_1 * n_2)
print(n_1 / n_2)
print(n_1 ** n_2)
print(n_1 // n_2)
print(n_1 % n_2)

num_3 = input('Введите первое число = ')
num_4 = input('Введите второе число = ')
print(num_3, type(num_3))
print(num_4, type(num_4))

num_5 = int(num_3) +10
num_6 = int(num_4) +100
print(num_5, type(num_5))
print(num_6, type(num_6))

num_7 = str(num_5) + '__OK'
num_8 = str(num_6) * 2 + num_7
print(num_7, type(num_7))
print(num_8, type(num_8))