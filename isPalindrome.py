# returns true if the provided string is a palindrome. Otherwise returns false

def isPalindrome(s):
    
    leftPointer = 0
    rightPointer = 0

    if len(s) % 2 == 0:
        leftPointer = len(s)//2
        rightPointer = leftPointer + 1
    else:
        leftPointer = len(s)//2
        rightPointer = leftPointer

    while leftPointer >= 0 and rightPointer < len(s):
        if s[leftPointer] != s[rightPointer]:
            return False
        leftPointer -= 1
        rightPointer += 1
    return True

string = "stanley yelnats"

print(isPalindrome(string))