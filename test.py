scopes = {'global': {'global': {'global': {'global': {}, 'variables': set()}, 'variables': set()}, 'variables': set()},
          'variables': set()}
n = 0


def check(d):
    global n
    for i in d:
        if type(d.get(i)) is dict:
            n += 1
            print('Hura', n, d.get(i))
            return check(d.get(i))


check(scopes)
