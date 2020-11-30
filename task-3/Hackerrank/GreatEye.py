t = int(input())
lst = []
sum = 0
for i in range(t):
    k = int(input())
    word = input()
    
    l = len(word.split())
    if l-1 >= k:
        output = word.split(' ')[k]
        lst.append(output)
    elif l-1 < k:
        lst.append("-1")

for i in range(t):
    if(lst[i] == "-1"):
        print("-1")
    else:
        for c in lst[i]:
            sum += ord(c)
        print(sum)
        sum = 0