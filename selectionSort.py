def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i 
        for j in range(i,n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    print(arr)

lst = [90,30,40,80,10]
selectionSort(lst)