def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return print (i)
        return print (-1)
       
firstUniqChar("loveleetcode")            
firstUniqChar("aabb")