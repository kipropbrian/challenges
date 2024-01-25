#28 https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

def strStr(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack) or len(needle) == 0:
        return -1
    
    for i in range(len(haystack)):
        if haystack[i] == needle[0] and haystack[i:i + len(needle)] == needle: #first character found
            return i


strStr("sadbutsad", "sad")