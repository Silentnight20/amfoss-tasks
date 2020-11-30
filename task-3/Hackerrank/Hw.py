t = int(input())
lst1 = []
lst2 = []

for i in range(t):
    n = int(input())
    lst1.append(n)

n1, n2, n3 = 1, 2, 3
count = 0
while count < max(lst1):
    lst2.append(n1)
    nth = (n1 + n2 + n3) % 1000000007
    n1 = n2
    n2 = n3
    n3 = nth
    count += 1

for i in range(t):
    y = lst2[lst1[i]-1]
    rev = 0
    
    print(int(str(y)[::-1]))