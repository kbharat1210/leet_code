def binaryadd(a,b):
    result=""
    carry=0

    a = a[-1::]
    b = b[-1::]

    for i in range(max(len(a),len(b))):
        digit_a = int(a[i]) if i < len(a) else 0
        digit_b = int(b[i]) if i < len(b) else 0

        total = digit_a + digit_b + carry
        total = total%2
        result = str(result)+str(total)
        carry = total//2

        if carry:
            result = '1'+ result

        return result

binaryadd('101','101')
