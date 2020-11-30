n, m = input().split()

lst1 = [int(x) for x in input().split()]

bool = False
set1 = set(lst1)

for i in range(int(n)):
    x = int(m) - lst1[i]
    if x in set1:
        bool = True
        break
print(bool)