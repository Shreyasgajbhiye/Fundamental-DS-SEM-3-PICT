# row = int(input("Enter the no. of rows : "))
# col = int(input("Enter the no. of col. : "))
# l1=[]
# l2=[]
# l3=[]
# for i in range(row):
#     temp=[]
#     for j in range (col):
#         val = int(input(f"Enter number a[{i}] b[{j}] : "))
#         temp.append(val)
#     l1.append(temp)
# for i in range(row):
#     temp=[]
#     for j in range (col):
#         val = int(input(f"Enter number a[{i}] b[{j}] : "))
#         temp.append(val)
#     l2.append(temp)

# for i in range(row):
#     temp=[]
#     for j in range (col):
#         val = l1[i][j] + l2[i][j]
#         temp.append(val)
#     l3.append(temp)

# print(l3)


# row = int(input("Enter the no. of rows : "))
# col = int(input("Enter the no. of col. : "))
# l1=[]
# l2=[]
# l3=[[0,0],[0,0]]
# for i in range(row):
#     temp=[]
#     for j in range (col):
#         val = int(input(f"Enter number a[{i}] b[{j}] : "))
#         temp.append(val)
#     l1.append(temp)
# for i in range(row):
#     temp=[]
#     for j in range (col):
#         val = int(input(f"Enter number a[{i}] b[{j}] : "))
#         temp.append(val)
#     l2.append(temp)

# for i in range(row):
#     temp=[]
#     for j in range (col):
#         for k in range (row):
#             l3[i][j] += l1[i][k] * l2[k][j]


# print(l3)

lst1 = [[1,2,3],[4,5,6],[7,8,9]]
lst2 = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        lst2[i][j] = lst1[j][i]
print(lst2)