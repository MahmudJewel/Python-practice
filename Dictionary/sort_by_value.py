#sort by value
dic={2:90, 1: 100, 8: 3, 5: 67, 3: 5}
dic2=sorted(dic.items(), key=lambda x:x[1])
print(dic2)