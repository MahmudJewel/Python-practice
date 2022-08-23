""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
'*****************************   Jewel Mahmud   *****************************'
'*****************************  CSE-13th,MBSTU  *****************************'
'***************************** Date: 08-05-2020 *****************************'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Strings are immutable. It does not support delete or insert.
#But we can assing new string.
#here is a trick or removing string

str='abcdefgh'
str.replace(str[1],'')
print(str)  #not remove
str=str.replace(str[1],'')
print(str) #now works