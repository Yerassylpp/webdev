def xor(a,b):
    if (a and not b or not a and b):
        return 1
    else:
        return 0  

n = input().split()
a = int(n[0])
b = int(n[1])  

print(xor(a,b))