lst = [1,2,3,4,5,6,7,8,9]
n = int(input("Enter the number to be search : "))
i=0
while i < len(lst):
    if lst[i] == n:
        print ("Element found at ", i)
    i+=1

