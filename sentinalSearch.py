lst =[1,2,3,4,5,6,7,8,9]
length = len(lst)-1
key = int(input("Enter the element to be search : "))
last = lst[length]
lst[length] = key
i=0
while lst[i]!=key:
    i+=1

if (i <= length ) or (arr[i] == key):
    print("Found at ",i)
else:
    print("Not found")