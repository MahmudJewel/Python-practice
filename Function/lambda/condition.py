# single condition ==> if else
single_lambda = lambda x,y : print(f"{x}>{y}") if x> y else print(f"{x}<{y}")
single_lambda(10,7)

# multiple condition ==> if elif else
multiple_lambda = lambda a,b: print(f"a>b") if a>b else print(f"a<b") if a<b else print(f"a==b")

multiple_lambda(5,5)

# No parameter 
hello = lambda :print('Hello world')
hello()