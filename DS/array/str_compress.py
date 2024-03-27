def compress(chars):
    chars = "".join(chars)
    
    res = ''
    i = 1
    count = 1
    
    
    #TODO:edge case: empty, len 1
    if len(chars) == 0:
        return ""
    if len(chars) == 1:
        return chars + '1'
    
    
    while i < len(chars):
        if chars[i] == chars[i-1]:
            count += 1
        else:
            res = res + chars[i-1] + str(count)
            count = 1
        
        i+= 1
            
            
    res = res + chars[i-1] + str(count)
    return len([char for char in res])
    
  
    
    
    
    
    
    
    
    
    
    
    
    

print(compress(["a","a","b","b","c","c","c"]))
        
        