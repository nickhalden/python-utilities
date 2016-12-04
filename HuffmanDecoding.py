def Decoding(encodings, encodedstring):
    d = {}
    for charc in encodings:
        key = charc[1]
        value = charc[0]
        d[key] = value

    print d
    res = ''

    while encodedstring:
        for k in d:
            if encodedstring.startswith(k):
                res = res + d[k]
                encodedstring = encodedstring[len(k):]
    print res


a=dict()
encodings=[['A','1011'],['B','1111']]

Decoding(encodings,'10111111')