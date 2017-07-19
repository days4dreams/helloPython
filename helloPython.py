#learningPython

#comments in hash


#Vars declared as JS (Note, no ;)
my_variable = 10
#and can be re-assigned loosely, as:
my_loose_var = 3
my_loose_var = 9
print my_loose_var 
#output is 9


#Booleans follow, as:
a = True
b = False


#whitespace is used to structure code. Be careful with how you use it.
#bad practice use of whitespace:
def spam():
eggs = 12
return eggs

print spam()
#output: File 'python' / IndentationError


#best practise use of whitepace (you should indent with four spaces):
def spam():
	eggs = 12
	return eggs
print spam()


#Math operators follow, as:
addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9


#Exponentiation lets you combine math with other data types (EG booleans) and commands. 
eight = 2 ** 3
#we create a new variable called eight and set it to 8; the result of 2 to the power to 3 (2^3).
#we use ** instead of * or the multiplication operator.


#Modulo returns the remainder from a division. So, 3 % 2, will return 1
#because 2 goes into 3 evenly once, with 1 left over. EG:

spam = 3 % 2
#output will be 1


""" applying concepts to an example.
You've finished eating at a restaurant, and received this bill:

Cost of meal: $44.50
Restaurant tax: 6.75%
Tip: 15%
You'll apply the tip to the overall cost of the meal (including tax). """

meal = 44.50
tax = 6.75 / 100
tip = 15 / 100
#var tax set to decimal value of 6.75%. Decimal form of 6.75%; 6.75 / 100, equals 0.0675. Tip follows

meal = meal + meal * tax
#python allows to reassign in a single line (yes, you're allowed to reassign a variable in terms of itself!)

total = meal + meal * tip
print total


#strings need to be within quotes (double of single)
name = "Ryan"
my_name = 'Lauren'


#Escaping characters
#Therefore some characters that cause problems. EG:

There's a snake in my boot!'
#breaks because Python thinks the apostrophe ends the string. We use the backslash to fix:

'There\'s a snake in my boot!'


#Each character in a string is assigned an index. 

c = "cats"[0]
n = "Ryan"[3]
#we create a new variable called c and set it to "c", the character at index zero of the string "cats".
#in Python, we start counting the index from zero instead of one.


#string methods, EG
len()
lower()
upper()
str()

parrot = "Norwegian Blue"
print len(parrot)

parrot.lower() 
#output "norwegian blue"

#Dot Notation. Methods that use dot notation only work with strings.
#len() and str() can work on other data types, as:

lion = "roar"
len(lion)
lion.upper()


#String Concatenation

print "Life " + "of " + "Brian"
#will print out the phrase Life of Brian.

print "I have " + str(2) + " coconuts!"
#will print I have 2 coconuts!

name = "Mike"
print "Hello %s" % (name)
#The % operator after a string combines a string with variables. 
#The % operator will replace a %s in the string with the string variable that comes after it.

#it can be used as below, to capture input and add to string:
name = raw_input("What is your name?")
quest = raw_input("What is your quest")

print "Ah, so your name is %s, and your quest is to %s" % (name, quest)
