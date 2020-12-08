a = 0
b = 0
k = 0
for n in range(1, 101):
    k = n * n
    a = k + a
for n in range(1, 101):
    b = n + b

print(b*b - a)
