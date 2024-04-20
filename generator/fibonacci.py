def generate_fibonacci():
    n1,n2=0,1
    while True:
        yield n1
        n1,n2=n2,n1+n2

seq = generate_fibonacci()
print(next(seq)) # 0
print(next(seq)) # 1
print(next(seq)) # 1
print(next(seq)) # 2
print(next(seq)) # 3
print(next(seq)) # 5

