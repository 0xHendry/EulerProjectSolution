
all_palindroms = []
for i in range(100, 1000):
    for n in range(100, 1000):
        number = str(i*n)
        a = number[::-1]
        if number == a:
            all_palindroms.append(int(a))
            print("palindrom")
            print(i, n, number)
print(max(all_palindroms))
