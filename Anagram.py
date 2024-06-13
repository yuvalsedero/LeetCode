
def isAnagram(s, t):
        s_list = []
        t_list = []
        if len(t) != len(s):
                return False
        for i in range(len(s)):
                s_list.append(s[i])
                t_list.append(t[i])
        s_list.sort()
        t_list.sort()
        lll= ''.join(s_list)
        ttt = ''.join(t_list)
        if lll == ttt:
                return True 
        return False

s = "rat"

t = "car"

print (isAnagram(s, t))