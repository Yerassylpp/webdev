n = int(input())
mass = list(map(int, input().split()))
cnt = 0
for i in mass:
    if (i>0):
        cnt=cnt+1
print(cnt)        