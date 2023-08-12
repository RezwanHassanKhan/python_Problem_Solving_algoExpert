# Two Number Sum

#Understanding the problem
#Given an array of dictinct value and a targetSum , we have to find the 2 values from the array that adds up to target sum.__dict__
#if value1,value2 adds up to targetSum > Return array[value1,value2]
#else > return empty array[]
#array =[3, 5, -4, 8, 11, 1, -1, 6],
#targetSum = 10
#output =[11,-1] or [-1,11]


#

### Approach 1
#Iterate through the array. For each number, iterate through the rest of the array; if adding any number in the rest of the array to the number yields the target sum, return the pair.
### Implementation

def twoNumberSum(array,targetSum):
    nums={}# this array set Bolean = True for all unique value in array
    for num in array:
        potentialMatch = targetSum - num  # tS=pM+num
        if potentialMatch in nums : #chk if pM already there in nums array
            return [potentialMatch,num] # chl
        else:
            nums[num]=True #Set bolean True for the unique num
    return [] #this return empty array if there are no pM in nums

### Complexity Analysis
#- Time Complexity: O(N), where N is the length of the input array.
#- Space Complexity: O(N).
