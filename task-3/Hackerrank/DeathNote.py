n = int(input())
lst1 = []
lst2 = []
lst3 = []
lst1 = [int(page) for page in input().split()] 
lst2 = [page for page in input().split()] 
lst1 = [int(i) for i in lst1]
lst2 = [int(i) for i in lst2]

for i in range(n):
    quotient = lst2[i]//lst1[i]
    lst3.append(quotient)
lst3.sort()
print(lst3[0])