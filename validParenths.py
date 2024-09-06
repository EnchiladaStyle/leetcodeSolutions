def validParenths(s):
    stack = ""
    pairs = {"}": "{", ")": "(", "]": "["}
    opens = "{(["

    for parenth in s:
        if parenth not in opens and stack == "":
            return False
        if parenth in opens:
            stack += parenth
        else:
            if stack[-1] == pairs[parenth]:
                stack = stack[:len(stack)-1]
            else:
                return False

    if stack != "":
        return False
    return True


parenths = "{{}[{}[](])]()}"

print(validParenths(parenths))



