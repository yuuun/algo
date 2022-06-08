n, atk = map(int ,input().split())
maxHp, curHp, damage = 0, 0, 0
for _ in range(n):
    t, a, h = map(int, input().split())
    if t == 1:
        tmp = h % atk
        if tmp == 0:
            damage = -(a * (h // atk - 1))
        else:
            damage = -(a * (h // atk))
    else:
        atk += a
        damage = h
    curHp += damage
    if curHp > 0:
        curHp = 0
    maxHp = max(maxHp, abs(curHp))
print(maxHp + 1)