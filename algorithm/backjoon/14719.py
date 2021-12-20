input()
arr = list(map(int, input().split()))
lt, rt = 0, len(arr)-1
lt_max, rt_max = arr[lt], arr[rt]
answer = 0
while lt < rt:
    if lt_max <= rt_max:
        lt += 1
        lt_max = max(lt_max, arr[lt])
        answer += lt_max-arr[lt]
    else:
        rt -= 1
        rt_max = max(rt_max, arr[rt])
        answer += rt_max-arr[rt]

print(answer)
