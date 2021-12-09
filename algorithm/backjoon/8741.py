n = int(input())
tmp = 2 ** n-1
sum = tmp * (tmp+1) // 2
print(bin(sum)[2:])