def solution(x):
    s = ''
    for c in x:
        b = ord(c)
        if b > 96 and b < 123:
            b = 219 - b
        s += chr(b)
    return s
