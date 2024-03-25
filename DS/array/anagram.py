import collections

def anagram(s,t):
    s = s.replace(' ','').lower()
    t = t.replace(' ','').lower()

    return sorted(s) == sorted(t)

def anagram2(s,p):
    return collections.Counter(s) == collections.Counter(p)
         


def anagram3(s,p):
    if len(s)!= len(p):
        return False

    mapping = {}
    for char in s:
        if char not in mapping:
            mapping[char] = 1
        else:
            mapping[char] += 1

    for char in p:
        if char in mapping:
            mapping[char] -= 1
        else:
            return False
    for c in mapping.values():
        if c != 0:
            return False
        
    return True






if __name__ == "__main__":
    print(anagram3('shirin','nooshin'))
