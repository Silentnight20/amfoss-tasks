n = int(input())
input = str(input())

counter0, counter1 = 0,0
for i in range(n):
    if input[i] == '0':
        counter0 += 1
    else:
        counter1 += 1

if (counter1 != counter0):
    print("1")
else:
    print("2")