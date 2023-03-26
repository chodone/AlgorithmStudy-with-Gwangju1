H, M = map(int, input().split())

# 0 <= M <= 44 -> H 1감소(0일때 23으로), M + 60 -45
if 0 <= M <= 44:
    if H != 0:
        H -= 1
        M += 60 - 45
    else:
        H = 23
        M += 60 - 45
else:
    M -= 45


print(H, M)
