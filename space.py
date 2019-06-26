# Scopes
scopes = {'global': {'parent': None, 'vars': set()}}

for i in range(int(input())):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        scopes.update({arg: dict(namesp)})
    if cmd == 'add':
        scopes['vars'].add(arg)
    print(i, cmd, namesp, arg, scopes)


