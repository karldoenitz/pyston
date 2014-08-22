l = 2L
print l
print type(l)

t = 1L
for i in xrange(150):
    t *= l
    print t, repr(t)

def test(a, b):
    print a, b
    print a + b, b + a, a.__add__(b), b.__add__(a)
    print a - b, b - a, a.__sub__(b), b.__sub__(a)
    print a * b, b * a, a.__mul__(b), b.__mul__(a)
    print a / b, b / a, a.__div__(b), b.__div__(a)


print 1L / 5L
print -1L / 5L
print 1L / -5L
print -1L / -5L

for a in [-5, -1, 1, 5, -2L, -1L, 1L, 2L]:
    for b in [-5, -1, 1, 5, -2L, -1L, 1L, 2L]:
        test(a, b)

print (2L).__rdiv__(-1)
print (2L).__rdiv__(-1L)
print (-2L).__rdiv__(1L)
print (-2L).__rdiv__(1)
