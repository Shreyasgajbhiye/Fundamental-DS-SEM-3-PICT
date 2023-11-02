# str = input("Enter the string : ")
# split_str = str.split()
# m=0
# word = 0
# for i in range(len(split_str)):
#     if m < len(split_str[i]):
#         m = len(split_str)
#         word = i
# print("Longest string is ",split_str[word])

# print ("Occurance of char in string ------------")
# x = input("Enter the string : ")
# y = input("ENter the char : ")
# a=0
# for i in range (len(x)):
#     if y==x[i]:
#         a=a+1
# print ("Occurance of ",y , " is " , a)

# print ("Wheather the string is palindrome or not ------------")
# q = input("Enter the string to check : ")
# temp = q
# if q == temp[::-1]:
#     print("YES its palindorme")
# else:
#     print("NO its not palimdrome")

# print ("first apperance ------------")
# one = input("Enter the string : ")
# two = input("Enter the substr : ")
# x=0
# y=0
# o=0
# for i in range (len(one)):
#     if two[y] == one[i]:
#         flag = 1
#         y=y+1
#         if y == len(two):
#             x =  i-(len(two) -1)
#             break    
#     else:
#         flag=0
#         y=0
# print(x)

strg = input("Enter the string : ")
count = dict()
lst = strg.split()
for word in strg:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)