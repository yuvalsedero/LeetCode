class Solution(object):
    def containsDuplicate(nums):
        myset = set(nums)
        if len(myset) != len(nums):
            return True
        else:
            return False
num = [1,2,3,1]
print (Solution.containsDuplicate(num))
        
                

        