def find_gens(m, f, gens):
    if m == 1 and f == 1:
        return gens
    elif m < 1 or f < 1 or m == f:
        return float('inf')
    if f > m:
        m, f = f, m
    factor = (m // f) - (float(m) / float(f)).is_integer()
    return find_gens(m - f * factor, f, gens + factor)


def solution(x, y):
    gens = find_gens(int(x), int(y), 0)
    if gens == float('inf'):
        return 'impossible'
    return str(gens)
