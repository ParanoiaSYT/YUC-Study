def f383(s, k):
    if len(s) <= k:
        return '0'
    l = 0
    while k > 0 and l < len(s) - 1:
        if s[l] > s[l + 1]:
            s = s.replace(s[l], '', 1)
            k -= 1
        else:
            l += 1
        while l > 0 and s[l-1] > s[l]:
            l -= 1
    s = s[:-k] if k else s
    return s.lstrip('0') or  '0'
print(f383('14329219',3))
print(f383('12354',3))

a='32455'
a=a.replace(a[0],'',1)
print(a[0])
print(a,a.lstrip('3'))