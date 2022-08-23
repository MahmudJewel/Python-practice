alphabet=['a','b','d','e','f','g','h','i','j']

def checkVowel(alphabet):
    vowel=['a','e','i','o','u']
    if(alphabet in vowel):
        return True
    else:
        return False

abc=filter(checkVowel,alphabet)

for i in abc:
    print(i)
