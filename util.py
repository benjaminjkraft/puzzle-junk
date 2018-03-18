def a1b2(s):
    return sum(ord(x) - ord('a') + 1 for x in s.lower().replace(' ', ''))


ord1 = a1b2


def chr1(n):
    return chr(ord('a') - 1 + n)
