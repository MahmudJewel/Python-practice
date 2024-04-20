def generate_odd_number():
    n1 = 1
    while True:
        yield n1
        n1 += 2

seq = generate_odd_number()
print(next(seq)) # 1
print(next(seq)) # 3
print(next(seq)) # 5
print(next(seq)) # 7
print(next(seq)) # 9
print(next(seq)) # 11

