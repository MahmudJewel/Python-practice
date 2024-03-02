#Using for loop
letter=[]
for i in "human":
    letter.append(i)
#print(letter)

#List comprehension
# ar=[ i for i in "human"]
# print(ar)

# # even number using list comprehensions 
# even=[i for i in range(1,20) if i%2==0]
# print('Even', even)

odd = [i for i in range(20) if i%2==1]
print(odd)
