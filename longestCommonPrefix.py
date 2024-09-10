
#returns the prefix that is shared by all items in the list

def longestCommonPrefix(strings):
    answer = strings[0]
    for word in strings:
        answer = answer[:len(word)]
        for i in range(len(answer)):
            if answer[i] != word[i]:
                answer = answer[:i]
                break
    return answer

print(longestCommonPrefix(["abc", "abcdef", "abracadabra"]))