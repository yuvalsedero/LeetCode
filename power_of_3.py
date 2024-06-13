def isPowerOfThree(n):
        """
        :type n: int
        :rtype: bool
        """
        third_sqr_n = n**(1/3)
        if third_sqr_n%1==0 and third_sqr_n != 0:
            return True
        else:
            return False
        
        
isPowerOfThree(-1)