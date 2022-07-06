#!/usr/bin/python3
ans = [[1], [1, 1]]


def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return ans[:1]
    if n == 2:
        return ans[:2]

    index = n - 2
    if index < len(ans):
        tmp = list()
        tmp.append(1)
        i = 0
        while i + 1 < len(ans[index]):
            val = ans[index][i] + ans[index][i + 1]
            tmp.append(val)
            i += 1

        tmp.append(1)
        ans.append(tmp)
    else:
        pascal_triangle(n - 1)
        pascal_triangle(n)

    return ans[:n]
