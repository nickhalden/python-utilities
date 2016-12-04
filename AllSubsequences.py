"""All subsequences powerset-[]"""



# A Naive recursive Python implementation of LCS problem

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0;
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1);
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n));

def kmp_search(pattern, text):
    if pattern == "":
        return 0  # Immediate match

    # Compute longest suffix-prefix table
    lsp = [0]  # Base case
    for c in pattern[1:]:
        j = lsp[-1]  # Start by assuming we're extending the previous LSP
        while j > 0 and c != pattern[j]:
            j = lsp[j - 1]
        if c == pattern[j]:
            j += 1
        lsp.append(j)

    # Walk through text string
    j = 0  # Number of chars matched in pattern
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lsp[j - 1]  # Fall back in the pattern
        if text[i] == pattern[j]:
            j += 1  # Next char matched, increment position
            if j == len(pattern):
                return i - (j - 1)
        return None  # Not found
# Driver program to test the above function
"""abc
"""


def maxLength(a, k):
    results = []
    print a, k

    for elem in powerset(a):
        if len(elem) != 0:
            results.append(elem)
    maxi = 0
    sum = 0
    for eachElement in results:
        for element in eachElement:
            sum = sum + int(element)
        if sum < k:
            if maxi < len(eachElement):
                maxi = len(eachElement)

    print 'aaa', maxi


def powerset(s):
    n = len(s)
    masks = [1 << j for j in xrange(n)]
    for i in xrange(2 ** n):
        yield [s[j] for j in range(n) if (masks[j] & i)]

if __name__ == '__main__':
    results=[]
    input1=list('abc')
    for elem in powerset(input1):
        if len(elem) !=0: results.append(elem)

    print results
    X = "AGGTABAxyz"
    Y = "GXTXAYGGBpqrz"
    print "Length of LCS is ", lcs(X, Y, len(X), len(Y))



