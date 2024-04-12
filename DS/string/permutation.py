import collections
from collections import Counter


##another approach: sort both then compare

def str_permutation(s1, s2):
    
    if len(s1) > len(s2):
        return False
    
    cnt1, window_count = Counter(s1), Counter(s2[:len(s1)])
    if cnt1 == window_count:
        return True
    
    diff = len(s2) - len(s1)
    for i in range(diff):
        
        if cnt1 == window_count:
            return True
        char1, char2 = s2[i], s2[i+len(s1)]
        window_count[char1] -= 1
        
        if window_count[char1] == 0:
            del window_count[char1]
        
        window_count[char2] += 1
    return cnt1 == window_count
        
        
        
        

    
      
        
    

    

print(str_permutation('abi','shiba'))



