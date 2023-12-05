n = 10
answer = 0
for i in range(4,n+1):
    if i % 2 == 0:
        answer += 1
    if i % 3 == 0:
        answer += 1
print(answer)