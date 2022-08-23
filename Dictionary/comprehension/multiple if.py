
'***********************   Jewel Mahmud  ***********************************'
'***********************  CSE-13th,MBSTU  ***********************************'
'*********************** Date: 01-05-2020 ***********************************'

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict={a:b for (a,b) in original_dict.items() if b%2!=0 if b<40}
print(new_dict)