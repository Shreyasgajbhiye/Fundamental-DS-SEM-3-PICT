# def shellSort(arr):
#     size = len(arr)
#     gap  = size // 2
#     while gap>0:
#         for i in range(gap,size):
#             current = arr[i]
#             pos = i 
#             while pos>=gap and current<=arr[pos-gap]:
#                 arr[pos] = arr[pos-gap]
#                 pos = pos-gap
#             arr[pos] = current
#         gap = gap//2

# lst = [20,10,50,80,30]
# shellSort(lst)
# print(lst)
