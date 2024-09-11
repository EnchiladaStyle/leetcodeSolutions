# returns the mode of a list of numbers

def mode(nums):
    
    
    mostCommon = 0
    mostCommonCount = 0
    currentCount = 0

    for num in nums:
        currentCount = 0
        for num2 in nums:
            if num2 == num:
                currentCount += 1
                if currentCount > mostCommonCount:
                    mostCommonCount = currentCount
                    mostCommon = num
    return mostCommon



print(mode([1,2,3,2,4,5,7,3,4,5,4,8,4,9,4]))