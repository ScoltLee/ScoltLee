
def group_graduating(groups):
    cnt = [0] * 5
    ans = 0
    for elm in groups:
        cnt[elm] += 1

    curr = min(cnt[1], cnt[2])
    total = sum(groups)
    ans = 10 ** 18
    for x in range(0, total + 1, 3):
        if (total - x) % 4 == 0:
            g3 = x // 3
            g4 = (total - x) // 4
            tmp = list(cnt)
            pos = 0
            neg = 0
            for i in range(4, 0, -1):
                curr = min(g4, tmp[i])
                g4 -= curr
                tmp[i] -= curr
                neg += curr * (4 - i)
                pos += abs(curr * (4 - i))
            for i in range(4, 0, -1):
                curr = min(g3, tmp[i])
                g3 -= curr
                tmp[i] -= curr
                neg += curr * (3 - i)
                pos += abs(curr * (3 - i))

            for i in range(4):
                if tmp[i] > 0:
                    neg += tmp[i] * -i
                    pos += tmp[i] * i
            neg += g3 * 3 + g4 * 4
            pos += g3 * 3 + g4 * 4
            if neg == 0:
                ans = min(ans, pos // 2)
    if ans == 10 ** 18:
        return -1
    else:
        return ans
