#count how many times e inside of hello
"hello".count("e")

# upper and lower letters without change variable
var = "Happy Birthday"
print (var)
print(var.lower())
print(var.upper())

#upper and lower with variable change
var = var.upper()
print (var)
var = var.lower()
print (var)

#First letter only
var.capitalize()

#Title
var.title()

# Functions to return true or False ###############################################
###############################################
#check letters
var.islower()
var.isupper()
var.istitle()

#check letters (careful, space isn't a letter)
var.isalpha()

#check for number
var.isdigit()

#alphanumeric charaters only
var.isalnum()

# index at start of letter B will be 6 . It's a count of index that starts at 0
var = "happy birthday"
var.index("birthday")

# will return 6 like the index, but this one don't give error, if that fail, he return -1 and don't crash the program
var.find("birthday")
var.find ("1234444")

# Remove some itens from string
var = "000000happybirthday000"
var.strip("0")
 # will return 'happybirthday'