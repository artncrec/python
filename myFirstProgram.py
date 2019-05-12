a = [15, 'hello', 15.58, True]
b = [15, -128, 'hello', False]

c = list(zip(a, b))
d = list(map(list, c))
e = [15.55555, 0.1111, -9.5]
f = list(map(round, e))
print(c)
print(f)
print(type(a[3]))
print(type(b[1]))
