
def contain_duplicates(s):
    length = len(s)
    for i in range(length):
        for j in range(i+1, length):
            if s[i] == s[j]:
                return True
    return False


def optimal(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False
        
print(contain_duplicates([1, 2, 3]))
print(optimal([1, 2, 3]))