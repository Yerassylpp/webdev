n = int(input())
mass = list(map(int, input().split()))  
cnt = 0

for i in range(1,n):
    cur = mass[i]
    prev = mass[i-1]
    if (cur>prev):
        cnt=cnt+1
print(cnt)        