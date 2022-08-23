
#Sort by key in ascending order
dic={2:90, 1: 100, 8: 3, 5: 67, 3: 5}
dic2={}
for i in sorted(dic):
	dic2[i]=dic[i]
print(dic2)
#print(sorted(dic))


#using lambda
#sort by value
my_dict = {2: 10, 1: 2, -3: 1234}
my_dict2=sorted(my_dict.items(), key=lambda x:x[0])
print(my_dict2)
