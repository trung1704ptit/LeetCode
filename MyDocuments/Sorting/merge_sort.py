def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of array
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        # sorting the L
        merge_sort(L)

        # sorting the R
        merge_sort(R)

        i = j = m = 0

        # Copy data to temp arrays L and R
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[m] = L[i]
                i += 1
            else:
                arr[m] = R[j]
                j += 1
            m += 1

        
        # Checking if any elements was left
        while i < len(L):
            arr[m] = L[i]
            i +=1
            m +=1

        while j < len(R):
            arr[m] = R[j]
            j += 1
            m += 1

        return arr