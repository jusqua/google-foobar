def solution(l):
    l.sort(reverse=True)
    diff = sum(l) % 3

    while sum(l) % 3 != 0:
        rm = list(filter(lambda n: n % 3 == diff, l))
        if len(rm) != 0:
            l.remove(rm[-1])
        diff = 1 if diff == 2 else 2

    if not l:
        return 0

    return int(''.join(map(str, l)))
