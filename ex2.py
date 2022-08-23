def solve(s):
	return (' '.join(i.capitalize() for i in s.split(' ')))

s='hello 3g world'
print(solve(s))