""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 28-10-2021 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# creating class
class person:
    def __init__(self, name): #constructor
        self.name=name
        print('Initialized')
    
    def sayhello(self): #Methods
        print(f"Hello world!, I'm {self.name}")

    def __del__(self): #destructor
        print(f"Bye {self.name}")

# creating object
obj1 = person('Jewel')
obj1.sayhello()