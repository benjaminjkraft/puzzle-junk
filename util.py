def a1b2(s):
    return sum(ord(x) - ord('a') + 1 for x in s.lower().replace(' ', ''))
