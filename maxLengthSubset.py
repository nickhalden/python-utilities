"""creates subsets and calculates the max value of a subset less than quea to k """
def maxLength(a, k):
    results = []
    print a, k

    for elem in powerset(a):
        if len(elem) != 0:
            results.append(elem)
    """"""
    maxi = 0
    for eachElement in results:
        sum = 0
        for element in eachElement:
            sum = sum + int(element)
        if sum <= k:
            if maxi < len(eachElement):
                maxi = len(eachElement)

    print  maxi



def powerset(s):
    n = len(s)
    masks = [1 << j for j in xrange(n)]
    for i in xrange(2 ** n):
        yield [s[j] for j in range(n) if (masks[j] & i)]

maxLength([3,1,2,1],4)