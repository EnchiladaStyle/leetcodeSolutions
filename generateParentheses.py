class Solution(object):
    def generateParenthesis(self, n):
        
        answer = []

        def recursive(closes, opens, current):
            if len(current) == n*2:
                answer.append(current)
                return
            else:
                if opens < n:
                    recursive(closes, opens + 1, current + "(")
                if closes < opens:
                    recursive(closes + 1, opens, current + ")")
            return

        recursive(0, 0, "")
        return answer