variant_one=input('Enter varint one: ').strip().split()
variant_two=input('Enter varint two: ').strip().split()
variant_three=input('Enter varint three: ').strip().split()
combination=[]
for sz in variant_one:
    if(len(variant_two)!=0 and len(variant_three) !=0):
        for cl in variant_two:
            for st in variant_three:
                temp=sz+'/'+cl+'/'+st
                combination.append(temp)
    elif (len(variant_two)!=0 and len(variant_three) == 0):
        for cl in variant_two:
            temp=sz+'/'+cl
            combination.append(temp)
    elif (len(variant_two)==0 and len(variant_three) != 0):
        for st in variant_three:
            temp=sz+'/'+st
            combination.append(temp)
print('combination: ', combination)

# lst=[1,2,3,4]
# lst.append(5)
# print(lst)