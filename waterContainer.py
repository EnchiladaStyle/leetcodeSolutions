# given a list of heights and positions for potentail walls to a container, returns the maximum possible water ammount when choosing two of the walls

def maxArea(heights):
    largest = 0
    leftPointer = 0
    rightPointer = len(heights) - 1

    while leftPointer < rightPointer:
        area = (rightPointer - leftPointer) * min(heights[leftPointer], heights[rightPointer])
        if area > largest:
            largest = area
        if heights[leftPointer] < heights[rightPointer]:
            leftPointer += 1
        else:
            rightPointer -= 1

    return largest





#less optimal solution
'''
def maxArea(self, height):
        
    largest = 0

    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            area = (j - i) * min(height[i], height[j])
            if area > largest:                    largest = area
    return largest'''