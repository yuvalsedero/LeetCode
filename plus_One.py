def plusOne(digits):
    num = int(''.join(map(str, digits)))
    num += 1
    numlist = [int(digit) for digit in str(num)]
    return print (numlist)

plusOne([9])