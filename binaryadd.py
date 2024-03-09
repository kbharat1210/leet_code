def binaryadd(a,b):
    a = int(a,2)
    b = int(b,2)

    total = a + b

    binarytotal=bin(total)
    addbinary=binarytotal[2:]

    return addbinary



