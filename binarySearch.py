def binarySerach(lst,n):
    i=0
    low = 0
    high = len(lst)-1
    while low <= high:
        mid = (low+high)//2
        if n == lst[mid]:
            print("Found at ",mid)
            break
        elif n>lst[mid]:
            low = mid+1
        elif  n<lst[mid]:
            high = mid-1
        else:
            print ("not found")
lst = [1,2,3,4,5,6,7,8,9]
n = int(input("Enter the number to be : "))
binarySerach(lst,n)

