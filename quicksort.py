def quicksort(array):
    size = len(array) # Size of the array
    if size <= 1:  # Return array when there are only one or lower items
        return array 
    else:
        pivot = array.pop(int(size/2)) # Middle Number chosen 

    right = [] # Numbers bigger than pivot
    left = [] # Numbers lower than or equal to pivot

    for num in array:
        if num > pivot: # Append to the right sub array if greater
            right.append(num)
        else: # Append to left if not
            left.append(num)
    return quicksort(left) + [pivot] + quicksort(right) # Repeat the process until both arrays only have one number and combine them all 

print(quicksort([5,6,2,7,9,0,2,1,6,7,5,7,9,0,5,3,2,1,6]))