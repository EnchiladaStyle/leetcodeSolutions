class Solution(object):
    def letterCombinations(self, digits):

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        answer = []
        if digits == "":
            return answer

        def recursive(index, current):
            if len(current) == len(digits):
                answer.append(current)
                return
            else:
                for char in letters[digits[index]]:
                    recursive(index+1, current+char)
            return
        recursive(0, "")
        return answer