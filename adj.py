#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
#My solution:
def solution(inputArray):
    greater = -10000
    new = 0
    for i in range(0, len(inputArray)):
        if i < len(inputArray) - 1 :
            new = inputArray[i] * inputArray[i+1]
            if new > greater:
                greater = new
            else:
                greater = greater
    return greater
        
        
#Optimal solution:

def solution(inputArray):
    return max([inputArray[i] * inputArray[i+1] for i in range(len(inputArray)-1)])
