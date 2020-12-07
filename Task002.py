
first_number, second_number, summary = 0, 1, 0
while second_number <= 4000000:
    summary = summary + second_number if second_number % 2 == 0 else summary
    first_number, second_number = second_number, first_number + second_number
print(summary)
