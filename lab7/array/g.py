n = int(input())
mass = list(map(int, input().split()))  

print(*mass[::-1])