#receives a list of numbers and a target number. returns the indexes of the two numbers that add to the target

def twoSum(l, target):
    data = {}
    for i in range(len(l)):
        potentialMatch = target - l[i]
        if potentialMatch in data.keys():
            return [i, data[potentialMatch]]
        else:
            data[l[i]] = i

input = [1,5,7,2,13,9]
target = 10

print(twoSum(input, target))