people = set()
n = 0
for _ in range(int(input())):
    id_ = input()
    if id_ != 'ENTER':
        people.add(id_)
    else:
        n += len(people)
        people = set()
print(n + len(people))