'''''''''
#Perfect 2D list
mylist=[]  #empty list
row=int(input("Enter row "))
for i in range(row):
    mylist.append([input(),int(input())]) #Enter in new line

print(mylist)
'''

'''''''''
li=[]  #empty list
row1=int(input("Enter the row: "))
for i in range(row1):
    a=int(input())   #input in new-line
    b=int(input())
    li.append([a,b])
print(li)
'''
mylist3=[]  #empty list
row1=int(input("Enter the row: "))
for i in range(row1):
    a=list(map(int,input().split()))   #each row in oneline
    print(a)
    mylist3.append(a)
print(mylist3)

