list_a = [1, 2, 3]
list_b = [10, 20, 30]

#map must be passed through list, dicionary
a=map(lambda x, y: x + y, list_a, list_b)

# converting map object to set
numbersSquare = set(a)
print(numbersSquare)
