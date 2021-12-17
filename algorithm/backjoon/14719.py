input()
height = list(map(int, input().split()))

lt, rt = 0, len(height)-1
lt_high, rt_high = height[lt], height[rt]

answer = 0
while lt < rt:
    if lt_high <= rt_high:
        lt += 1
        lt_high = max(lt_high, height[lt])
        answer += lt_high - height[lt]
    else:
        rt -= 1
        rt_high = max(rt_high, height[rt])
        answer += rt_high - height[rt]

print(answer)
