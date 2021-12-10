n = int(input())
arr = list(map(int, input().split()))
x = int(input())

answer = 0

# arr.sort()
# lt, rt = 0, n-1
# while lt < rt:
#     sum = arr[lt] + arr[rt]
#     print(sum)
#     if sum == x:
#         answer += 1
#         lt += 1
#     elif sum < x:
#         lt += 1
#     else:
#         rt -= 1
#
# print(answer)



a_dict = {}
for i, v in enumerate(arr):
    if x - v in a_dict:
        answer += 1
    a_dict[v] = i
print(answer)

# for i, v in enumerate(arr):
#     res = x-v
#     if res in arr[i+1:]:
#         answer += 1
# print(answer)
