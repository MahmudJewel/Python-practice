""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'***********************   Jewel Mahmud   ***********************************'
'***********************  CSE-13th,MBSTU  ***********************************'
'*********************** Date: 01-05-2020 ***********************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""
#input with new line
myDict={}
for i in range(2):
    key=input()
    value=input()
    myDict[key]=value
print(myDict)
"""""

"""""""""
#one line input
myDict1={}
for i in range(2):
    key,value=input().split()
    myDict1[key]=value
print(myDict1)
"""""

"""""
#not expected why?
myDict2={input():int(input()) for _ in range(2)}
print(myDict2)
"""""

"""""""""
#create in one-line(string type)
myDict3=dict(input().split() for _ in range(2))
print(myDict3)
"""

#create in one-line (int type)
myDict4=dict(map(int,input().split()) for _ in range(2))
print(myDict4)

