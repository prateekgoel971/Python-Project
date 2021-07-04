#  How to access string character/ String Slicing ?
# It will always include first given index and excluse last given index
## Python slicing is about obtaining a sub-string from the given string by slicing it respectively from start to end.


##str = 'programiz'
##print(str)
##
####first character
##print(str[0:1])
##
###last character
##print(str[-1])
##
###slicing 2nd to 5th character
##print(str[1:5])
##
###slicing 6th to 2nd last character
##print(str[5:-1])

# -------------------------

s = 'HelloWorld'   #---dlrowolleh

print(s[:]) # -- :

print(s[::]) # --- ::

first_five_chars = s[:5] # --0:5
print(first_five_chars)

third_to_fifth_chars = s[2:5]
print(third_to_fifth_chars)

reverse_str = s[0:6:4] # ----- Imp : & ::
print(reverse_str)




s = 'Python'
print(s[2:-1])


str ='Pra','Vik','Mon'
print(type(str))
print(str[0:1])
