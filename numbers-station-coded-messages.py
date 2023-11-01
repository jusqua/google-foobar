def solution(l, t):
    for x in range(len(l)):
        for y in range(x, len(l)):
            if sum(l[x:y + 1]) == t:
                return [x, y]

    return [-1, -1]
