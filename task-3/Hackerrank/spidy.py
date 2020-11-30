t = int(input())
lst1 = []
lst2 = []

for i in range(t):
    n,k = input().split()

    lst1 = [int(bags) for bags in input().split()]
    
    lst1.sort()
    product = int(lst1.pop()) - int(k)

    for j in range(int(n) - 1):
        product = product * lst1[j]
    lst2.append(product)
    lst1.clear()
    product = 1

for i in range(t):
    print(lst2[i])