'''''''''
List = [ [1, 3, 5], [8, 5, 6], [7, 1, 6] ]
print(List[1])  #[8, 5, 6]

r,c=3,3
mylist = [ [0] * c ] * r  # with each element value as 0
print(mylist)  #[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

r,c = 3,4
Array = [ [0] * c for i in range(r) ]
print(Array)  #[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''

'''''''''
#Problem
r = int(input())
arr = [[] for i in range(r)]
arr.append([int(j) for j in input().split()])
print(arr)
'''

#Perfect 2D list
mylist=[]
row=3
for i in range(row):
    mylist.append([input(),int(input())])

print(mylist)