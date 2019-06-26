scopes = {'global': {'parent': None, 'variables': set()}}


def create(dict):
    if namesp in dict.keys():
        return create()



# def add():
#     pass
# def get():
#     pass


for i in range(int(input())):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        scopes.update({arg: dict(namesp)})
    if cmd == 'add':
        scopes['vars'].add(arg)
    if cmd == 'get':
        pass
    print(i, cmd, namesp, arg, scopes)
