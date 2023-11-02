def fibonacci(arr,x,n):
    fib2 = 0
    fib1 = 1
    fib = fib2+fib1

    while (fib < n):
        fib2 = fib1
        fib1 = fib 
        fib = fib2+fib1 
    offset = -1
    while (fib > 1):
        i = min (offset+fib2, n-1)

        if (arr[i] < x):
            fib = fib1 
            fib1 = fib2
            fib2 = fib-fib1 
            offset = i
        elif (arr[i] > x):
            fib = fib2
            fib1 = fib1-fib
            fib2 = fib2-fib1 
        else:
            return i 
    
    if (fib1 and arr[i] == x):
        return n-1
    else:
        return -1
lst=[10,20,30,40,50,60]
size = len(lst)
ind = fibonacci(lst,40,size)
if (ind > 0):
    print ("Found at " ,ind)
else:
    print ("Not Found  " ,ind)
