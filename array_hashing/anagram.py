def is_anagram(s,t):
    if len(t) != len(s):
        return False
    return sorted(s) == sorted(t)


def optimal(s, t):
    if len(s) != len(t):
        return False
    char_freq_count = {}
    for char in s:
        char_freq_count[char] = 1 + char_freq_count.get(char, 0)
    for char in t:
        if char not in char_freq_count:
            return False
        char_freq_count[char] =  char_freq_count.get(char, 0) - 1
        if char_freq_count[char] < 0:
            return False
    return True