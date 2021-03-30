n = int(input())
mass = list(map(int, input().split()))  
cnt = 0
flag = False
for i in range(1,n):
    cur = mass[i]
    prev = mass[i-1]
    if (cur>0 and prev>0 or cur<0 and prev<0):
        flag = True
if (flag):
    print("YES")
else:
    print("NO")          