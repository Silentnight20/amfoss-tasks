t = int(input())
lsti = []
lstmax = []
lstA = []

for x in range(t):
    n, m, k = input().split()
    lsti = [int(stones) for stones in input().split()]
    lstmax = [int(box) for box in input().split()]  
    lstmax.sort()
    
    if sum(lstmax[-int(k):]) >= sum(lsti):
        lstA.append("YES")
    else:
        lstA.append("NO")
    lsti.clear()
    lstmax.clear()
for i in range(t):
    print(lstA[i])