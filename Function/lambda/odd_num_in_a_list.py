arr = [1,2,3,4,5,6]
resMap = list(map(lambda x:x%2==0, arr))
resFilter = list(filter(lambda x:x%2==0, arr))
print(f"Map ==> {resMap}\nFilter ==> {resFilter}")