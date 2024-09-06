#returns the longest substring without repeating characters

def longestSubstring(s):
    
    q = ""
    longest = ""

    for char in s:
        if char not in q:
            q += char
            if len(longest) < len(q):
                longest = q
        else:
            while char in q:
                q = q[1:]
            q += char

    return longest

string = "Tree Top"

print(longestSubstring(string))

