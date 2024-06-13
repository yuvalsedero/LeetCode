def getConcatenation(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in nums*2:
            ans.append(i)
        return ans
        print (ans)
getConcatenation([1,3,2,1])