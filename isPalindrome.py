def isPalindrome(x):
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False

isPalindrome(x = 121)