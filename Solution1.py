# def getSubString(string):
#         r = set()
#         recursion(string, r)
#         return r

# def recursion(needAdd, r:set):
#         if needAdd not in r:
#                 r.add(needAdd)
#         else: return
#         recursion(needAdd[1:], r)
#         recursion(needAdd[0:-1], r)
#         return

# print(getSubString("abc"))

def Solution1(source, target):
        i = 0
        j = 0
        count = 0
        
        while j < len(target):
                start = j
                for i in range(len(source)):
                        if j < len(target) and source[i] == target[j]:
                                j += 1
                
                if start == j:
                        return -1
                
                count += 1
        
        return count

print(Solution1("abc", "abcbc"))
print(Solution1("abc", "acdbc"))
print(Solution1("xyz", "xzyxz"))