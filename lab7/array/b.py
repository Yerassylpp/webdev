n = int(input())
mass = list(map(int, input().split()))

for i in mass:
    if (i%2==0):
        print(i,end=" ")