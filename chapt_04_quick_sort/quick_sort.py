def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        # Recursive case
        pivot = arr[0]
        # Sub-array of all the elements  less than the pivot
        less = [i for i in arr[1:] if i <= pivot]
       
        # Sub-array of all the elements  greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]
       
        return quicksort(less) + [pivot] + quicksort(greater)