def twoSum(nums, target):
        for i in range(len(nums)):
            for n in range(len(nums)):
                if (nums[i] + nums[n])==target and i != n:
                    return print([i,n])
        else: print("nooo")
                    
        
twoSum(nums = [2,7,11,15], target = 9)
