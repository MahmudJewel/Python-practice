myDic=dict()
# Dictionary Methods
marks = {}.fromkeys(['Math', 'English', 'Science'], 0)

# Output: {'Math': 0, 'English': 0, 'Science': 0}
print(marks)

for item in marks.items():
    print(item)

# Output: ['English', 'Math', 'Science']
print(list(sorted(marks.keys())))

#normal structure
myDic1={}
for i in range(6):
    myDic1[i]=i*i
print(myDic1)

#comprehension
mydic2={x:x*x for x in range(6)}
print(mydic2)


