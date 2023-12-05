box = [10, 8, 6]
n = 3
answer = 1
for i in box:
    answer = answer * (i // n)
print(answer)