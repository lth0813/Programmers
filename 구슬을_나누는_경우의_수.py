balls = 3
share = 2
answer = 0
ball = 1
shares = 1
sub = 1
for i in range(1,balls+1):
    ball = ball * i
for j in range(1,share+1):
    shares = shares * j
for k in range(1,balls-share+1):
    sub = sub * k
answer = ball / (sub * shares)
print(int(answer))