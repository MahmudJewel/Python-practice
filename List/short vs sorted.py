#listname.sort()  >>sorted array are saved in listname
#sorted(listname) >>sorted array are not saved in listname

array=[2,6,4,3,8]
print(array.sort()) #not working why???

array.sort()
print(array)        #working


array=[2,6,4,3,8]
sorted(array)
print(array)       #not sorted

print(sorted(array)) #sorted
print(array)
