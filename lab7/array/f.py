n = int(input())
mass = list(map(int, input().split()))  
cnt = 0
flag = False
for i in range(1,n-1):
    cur = mass[i]
    prev = mass[i-1]
    nxt = mass[i+1]
    if (cur>prev and cur>nxt):
        cnt=cnt+1
print(cnt)         