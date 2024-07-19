def selection_sort(arr):
    
    # Get array size
    n = len(arr)

    for i in range(n):
        smallest_index = i
        # Find the smallest element in remaining unsorted array
        for j in range(i + 1, n):
            if (arr[j] < arr[smallest_index]):
                smallest_index = j
        
        # Swap the found smallest element with the first element of the unsorted array
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    # print sorte list
    print(arr)