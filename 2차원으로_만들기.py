num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948]
n = 3
answer = [ ]
tmp = [ ]
while len(num_list) != 0:
    while len(tmp) != n:
        for i in range(n):
            tmp.append(num_list[i])
    for j in range(n-1,-1,-1):
        num_list.pop(j)
    answer.append(tmp)
    tmp = [ ]
print(answer)
