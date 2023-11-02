def InsertionSort(arr):
    for i in range(1,len(arr)):
        j = i
        while arr[j-1] < arr[j] and j >0:
            arr[j-1], arr[j] = arr[j],arr[j-1]
            j-=1

lst = [30,10.50,20,70]
InsertionSort(lst)
print(lst) 