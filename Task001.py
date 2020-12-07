
i = 0
array = []
while i < 999:
    i += 1
    if (i % 3) == 0 or (i % 5) == 0:
        array.append(i)
print(sum(array))
