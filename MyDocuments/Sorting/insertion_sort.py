def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(n)):
        key = arr[i]

        """
        Move all elements of array arr[0...i-1], that are greater than key, to one position
        ahead of their current postion
        """

        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j+1] = key

        return arr