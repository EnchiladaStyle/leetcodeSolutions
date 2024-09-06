#returns the longest palindrome in a given string


def longestPalindrome(s):
    
    longest = ""
    current = ""

    for i in range(len(s)):
        leftPointer = i
        rightPointer = i

        while leftPointer >= 0 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
            current = s[leftPointer:rightPointer+1]
            if len(current) > len(longest):
                longest = current
            leftPointer -= 1
            rightPointer += 1

        leftPointer = i
        rightPointer = i+1

        while leftPointer >= 0 and rightPointer < len(s) and s[leftPointer] == s[rightPointer]:
            current = s[leftPointer:rightPointer+1]
            if len(current) > len(longest):
                longest = current
            leftPointer -= 1
            rightPointer += 1

    return longest

string = "stanleyl yelnats jijijij"

print(longestPalindrome(string))

