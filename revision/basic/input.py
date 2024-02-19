# date: 23-02-22

##  Input string by default.
# a=input('Enter something ', )
# print(a)

# # oneline input ==> list
# n = input().strip().split() # n will be list of string 
# print(type(n))
# print(n)

# n = list(map(int, input().strip().split())) # n will be list of int 
# print(n)

# # multiple variable in one line using tuple 
# (x,y,z) = input().split()
# print(x)

# # multiple variable in one line using list comprehension
# x,y,z = [int(x) for x in input().split()]
# print(z)

# # multiple line integer input 
# n = [int(input()) for _ in range(int(input()))]
# print(n)

# # normal way
# lst = []
# number = int(input())
# for i in range(number):
#     tmp = input()
#     lst.append(tmp)
# print(lst)

# simple way
lst = [input() for i in range(int(input()))]
print(lst)

