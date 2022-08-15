#################################################################################################################################################################
## Problem = So the problem is to rotate an array by one. It means that [1,2,3,4,5] will be rotated to [5,1,2,3,4]
## Solution = We will simply start swapping from last two elements of array so that we will get 5 in begining. It means that 5 will be swapped by 4 then 5 will be
##            swapped by 3 and then 5 will be swapped by 2 and so on.
#################################################################################################################################################################




def rotate(arr,n):
    #arr.append(0)
    new_ind = len(arr) -1
    while new_ind > 0:
        temp = arr[new_ind]
        arr[new_ind] = arr[new_ind-1]
        arr[new_ind-1] = temp
        new_ind = new_ind -1
        print(new_ind)
        print(arr)
    print(arr)

arr = [1,2,3,4,5]
k = rotate(arr,5)


#####################################################################
Output: 
3
[1, 2, 3, 5, 4]
2
[1, 2, 5, 3, 4]
1
[1, 5, 2, 3, 4]
0
[5, 1, 2, 3, 4]
##########################################################################################

##########################################################################################
Time complexity = O(n)
Sapce complexity = O(1)
##########################################################################################
