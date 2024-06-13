def buildArray(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return print(ans)

buildArray([5,0,1,2,3,4])