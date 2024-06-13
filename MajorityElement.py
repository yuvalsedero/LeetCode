def majorityElement(nums=list):
        """
        :type nums: List[int]
        :rtype: int
        """
        bigval = nums[0]
        for i in range(len(nums)):
            if nums.count(nums[i]) >=  nums.count(bigval):
                bigval = nums[i]
        return bigval    
                
nums = [3,2,3.4,6,3,3,4,5]
majorityElement(nums)