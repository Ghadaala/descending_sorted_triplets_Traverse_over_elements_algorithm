# descending_sorted_triplets_Traverse_over_elements_algorithm
 More_Affiant_ Algorithm: Traverse over elements,implimintation Python Code
In this solving problem, we try to develop an algorithm to find triplets in descending sorted elements in the array. We examine many data structure algorithms like tuples, and Stack; and in the end, we create a model that can take advantage of Tree data structure, Stack, and Tuples, as much as we can. The first brute force algorithm develops triple iterations, and three nested loops, over all possible triplets, can be found in the array. The first one iterates over all elements, it is a big outer loop. The second one is iterating over the elements and then setting the element at the right of the first element to form a big outer loop, it is an intermediate loop. Where the third loop iterates over the next right of the middle element, it is an inner loop. All these loops work to satisfy the condition of the main problem(maximum, middle, minimum) in values in descending sorted sub-lists. A time complexity hasO(n^3), and a space complexity is O(1).

      The second mixed-up algorithm is to conclude variable concepts. It traverses over the elements only once, one time, from right to left maintaining a constant time of each operation at each step. The time complexity for this algorithm is O(n), as one loop iterates over elements. Space complexity is O(1) because there is a constant amount of memory location to store three temporary variables: first, second, and third.
      In conclusion, the second algorithm seems to be more efficient than a brute force algorithm, since it takes less time for complexity and spatial memory. A brute force is not much efficient for a large number of elements even.


NOTE:
Another algorithm to solve this problem is using the merge sort algorithm. In this algorithm we take advantage of the divide and conquer method, to divide the list into two halves, then merge each sub-list generated in a descending sorted list, by calling the function itself recursively. It is an efficient sorting algorithm. 
Time complexity is O(nlogn)
I prefer to create the (TRAVERSE SORTING ALGORITHM) because it takes less time and complexity compared with the merge sort algorithm, still, we must acknowledge the importance of the merge sort algorithm as a general proposal in sorting list

Algorithm merge sort to find a descending sorted triplets
def findDescendingSortedTriplet (arr):
    n = len(arr)  # get the length of the array
    max_val = arr[0]  # initialize the maximum value to the first element of the array
    min_val = arr[0]  # initialize the minimum value to the first element of the array
    for i in range(1, n):  # iterate over the array starting from the second element
        if arr[i] < min_val:  # if the current element is less than the minimum value
            min_val = arr[i]  # update the minimum value
        elif arr[i] > max_val:  # else if the current element is greater than the maximum value
            max_val = arr[i]  # update the maximum value
        else:  # else if we have found a triplet
            return (max_val, arr[i], min_val)  # return the triplet (max_val, current element, min_val)
               #Call function in the output
findDescendingSortedTriplet (arr)
