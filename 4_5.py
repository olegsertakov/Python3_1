from functools import reduce
def func(x,y):
    print("({0}, {1})".format(x, y))
    return x * y


arr = [i for i in range(100, 1000 + 1) if i % 2 == 0]
print(arr)
multiplication = reduce(func, arr)
print(multiplication)
