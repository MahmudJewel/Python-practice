'''''''''
#one line input as you want.
#strip removes back and front space
input.strip().split()
split() is used to create a Python list out of a string. 
If no delimiter is given, this breaks the string by spaces. 
So, now we have: [“1”, “2”, “4”, “42”]
'''''

a=list (map (int, input().strip().split()))
print(a)

