nested=[[1,2],[2,3],[3,4],[2,4]]
flat = [a for sublist in nested for a in sublist]
flat2=[a for a,b in nested]
print(nested)
print(flat)
print(flat2)