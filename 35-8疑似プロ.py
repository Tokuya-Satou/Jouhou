def gcd(l, s):
    if l < s:
        s = s-l
        return gcd(l,s)
    elif l > s:
        l = l-s
        return gcd(l,s)
    else:
        print(l)

gcd(876,204)
