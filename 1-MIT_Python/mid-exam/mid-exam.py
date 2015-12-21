def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    Example:
    	>>> myLog(16, 2)
    	4
    	>>> myLog(15, 3)
    	2
    '''
    ans = 0
    while b ** ans < x:
    	ans += 1
    if b ** ans > x: return ans - 1
    return ans

def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    Example:
    	>>> s1 = 'abcd'
    	>>> s2 = 'efghi'
    	>>> laceStrings(s1, s2)
    	'aebfcgdhi'
    	>>> s1 = ''
    	>>> s2 = ''
    	>>> laceStrings(s1, s2)
    	''
    """
    ans = ''
    while s1 != '' and s2 != '':
        ans += s1[0]
        ans += s2[0]
        s1, s2 = s1[1:], s2[1:]  	
    return ans + s1 + s2

# To hard!
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    Example:
    	>>> s1 = 'abcd'
    	>>> s2 = 'efghi'
    	>>> laceStringsRecur(s1, s2)
    	'aebfcgdhi'
    	>>> s1 = ''
    	>>> s2 = ''
    	>>> laceStringsRecur(s1, s2)
    	''
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return out + s2
        if s2 == '':
            return out + s1
        else:
	    	return helpLaceStrings(s2, s1[1:], out + s1[0])
	    	# return helpLaceStrings(s1[1:], s2[1:], out + s1[0] + s2[0])
    return helpLaceStrings(s1, s2, '')

# def fixedPoint(f, epsilon):
#     """
#     f: a function of one argument that returns a float
#     epsilon: a small float
  
#     returns the best guess when that guess is less than epsilon 
#     away from f(guess) or after 100 trials, whichever comes first.
#     """
#     guess = 1.0
#     for i in range(100):
#         if abs(f(guess) - guess) < epsilon:
#             return guess
#         else:
#             guess = f(guess)
#     return guess

# def sqrt(a):
#     def tryit(x):
#         return 0.5 * (a/x + x)
#     return fixedPoint(tryit, 0.0001)



# def babylon(x):
#     def test(x):
#         return 0.5 * ((a / x) + x)
#     return test

# def sqrt(a):
#     global a
#     return fixedPoint(babylon(a), 0.0001)


def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    Example:
    	>>> McNuggets(15)
    	True
    	>>> McNuggets(16)
    	False
    """
    packages = (6, 9, 20)
    hasSolution = False
    for a in range(0, int(n / packages[0]) + 1):
        for b in range(0, int(n / packages[1]) + 1):
            for c in range(0, int(n / packages[2]) + 1):
                if n == packages[0] * a + packages[1] * b + packages[2] * c:
                    hasSolution = True
                    break
            if hasSolution == True: break
        if hasSolution == True: break
    return hasSolution