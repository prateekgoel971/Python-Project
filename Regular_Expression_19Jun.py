# --- regular Expression

import re

##var ="welcome to python programming"
##output = re.match("welcome",var)
##print(output)
##print(output.group())
##print(output.span())


##var ="Welcome to python programming"
##output = re.match("welcome",var,re.I)
##print(output)
##print(output.group())
##print(output.span())
##
##
##var ="Welcome to python programming"
##output = re.search("python",var,re.I)
##print(output)
##print(output.group())
##print(output.span())
##
##
##var ="<html><body><head>" # Greedy Method
##output = re.search("<.*>",var)
##print(output.group())
##
##
##var ="<html><body><head>"
##output = re.search("<.*?>",var) # ? is non greedy method 
##print(output.group())
##
##
##var ="Sachin is greatest than lara " 
##output = re.search(".* is .*",var)
##print(output.group())
##
##
##var ="Sachin is greatest than lara " 
##output = re.search("(.*) is (.*)",var)
##print(output.group())
##print(output.group(1))

##var ="Sachin is greatest than lara " 
##output = re.search("(.*) is (.*?) (.*)",var)
##print(output.group())
##print(output.group(1))
##print(output.group(2))
##print(output.group(3))


##var ="INDIA scored 423 against SriLanka in 49.4 overs in 2013 with 8 runs per over"
##output = re.findall('\d{1,3}',var) # \d means it will print all the numbers in output {1,3} means maximum of 3 digit give output in form of list 
##print(output)
##
##
##var ="INDIA scored 423 against SriLanka in 49.4 overs in 2013 with 8 runs per over"
##output = re.findall('\D{1,4}',var) # \D means it will print all the digit in output {1,4} means maximum of 4 digit give output in form of list 
##print(output)


##var ="INDIA scored 423 against SriLanka in 49.4 overs in 2013 with 8 runs per over"
##output = re.findall('\w',var) # \w means it will print all the string in output as a single character  (Special Character )
##print(output)
##
##
##var ="INDIA scored 423 against SriLanka in 49.4 overs in 2013 with 8 runs per over"
##output = re.findall('\w*',var) # \w* means it will print all the string with space 
##print(output)
##
##var ="INDIA scored 423 against SriLanka in 49.4 overs in 2013 with 8 runs per over"
##output = re.findall('\w+',var) # \D means it will print all the string without space
##print(output)

##var ="INDIA scored 423 against SriLanka in 49.4 overs in 2013 with 8 runs per over"
##output = re.findall('\W',var) # \w means it will print all the spaces 
##print(output)


##var = "Asia and China are same "
##output = re.findall('[a-ca-z]*',var)
##print(output)
##
##
##var = "Asia and China are same "
##output = re.findall('[A-Ca-z]*',var)
##print(output)
##
##
##var = "Asia and China are same "
##output = re.sub('A','a',var)
##print(output)
##
##var = "Asia and China are same "
##output = re.split('a',var)
##print(output)
##
##
##
##\   Used to drop the special meaning of character
##    following it (discussed below)
##[]  Represent a character class
##^   Matches the beginning
##$   Matches the end
##.   Matches any character except newline
##?   Matches zero or one occurrence.
##|   Means OR (Matches with any of the characters
##    separated by it.
##*   Any number of occurrences (including 0 occurrences)
##+   One or more occurrences
##{}  Indicate number of occurrences of a preceding RE 
##    to match.
##()  Enclose a group of REs
