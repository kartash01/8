def ght(a, o):
    i = 1
    while i < o:
        a.remove(max(a))
        i += 1
    return max(a)