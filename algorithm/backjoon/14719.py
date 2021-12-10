h, w = map(int, input().split())
height = list(map(int, input().split()))

lt, rt = 0, w-1

lt_max, rt_max = height[lt], height[rt]
answer = 0
while lt < rt:
    lt_max = max(lt_max, height[lt])
    rt_max = max(rt_max, height[rt])
    if lt_max <= rt_max:
        answer += lt_max - height[lt]
        lt += 1
    else:
        answer += rt_max - height[rt]
        rt -= 1

print(answer)