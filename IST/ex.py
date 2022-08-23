ab=''
a=[2,3,4,5]
a=set(a)
for i in sorted(a):
	ab=ab+str(i)+','
print(ab.strip(','))
print(type(a))