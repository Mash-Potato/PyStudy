a = int(input())
b = int(input())
rt = len(str(b))-1
while rt >= 0:
    print(a*int(str(b)[rt]))
    rt -= 1
print(a*b)