s = "10 20 30 Z 40"
answer = 0
s = s.split(" ")
for i in range(len(s)):
    if s[i] != 'Z':
        answer += int(s[i])
    elif s[i] == 'Z':
        answer = answer - (int(s[i-1]) + int(s[i-1]))
print(answer)