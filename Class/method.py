class parrot:

	 # instance attributes
	def __init__(self,name,age):
		self.name=name 
		self.age=age

	# instance attributes
	def sing(self,song):
		print('{} sings {}'.format(self.name,song))

	def dance(self):
		return ('{} is now dancing'.format(self.name))


#creating object
blu=parrot('Doyel',10)

blu.sing('traditional song')

print(blu.dance())
