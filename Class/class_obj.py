# class Parrot:

#     # class attribute
#     species = "bird"

#     # instance attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # instantiate the Parrot class
# blu = Parrot("Blu", 10)
# woo = Parrot("Woo", 15)

# # access the class attributes
# print("Blu is a {}".format(blu.species))
# print("Woo is also a {}".format(woo.species))

# # access the instance attributes
# print("{} is {} years old".format( blu.name, blu.age))
# print("{} is {} years old".format( woo.name, woo.age))

# human with name and age 
class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_hobby(self, hobby_name):
        print(f"{self.name}'s age is {self.age} and hobby is {hobby_name}")

obj1 = Human('Jahid', 17)
obj2 = Human('Milon', 27)
obj1.get_hobby('Gardening')
obj2.get_hobby('Sleeping')
