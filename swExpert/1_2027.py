val = 5
for idx in range(0, val):
    for i in range(0, val):
        if idx == i:
            print("#", end="")
        else:
            print("+", end="")
    print()