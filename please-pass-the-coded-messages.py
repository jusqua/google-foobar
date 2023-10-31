def solution(l):
    l.sort(reverse=True)
    diff = sum(l) % 3
    ml = 0
    while sum(l) % 3 != 0:
        rm = list(filter(lambda n: n % 3 == diff, l))
        if len(rm) > ml:
            for e in rm[-1 - ml:]:
                l.remove(e)
        diff = 1 if diff == 2 else 2
        ml += -ml
    if not l:
        return 0
    return int(''.join(map(str, l)))
