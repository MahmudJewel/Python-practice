# generator 
def my_generator(n):
    value = 0
    while value < n:
        # produce the current value of the counter
        yield value
        value += 1
# iterate over the generator object produced by my_generator
for value in my_generator(3):
    print(value)

#
0
1
2

