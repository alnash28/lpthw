#Ch. 5 More Variables and Printing

#A string is how you make something that your program might give to a human. You print them, save
#them to files, send them to web servers, all sorts of things. Strings are really handy, 
#so in this exercise you will learn how to make stings that have variables embedded in them

my_name = 'Alfredzo Nash'
my_age = 29 # Not a lie 
my_height = 71 # inches 
my_weight = 270 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Lets talk about %s." % my_name
print "He`s %d inches tall." % my_height
print "He`s %d pounds heavy." % my_weight
print "Actually that`s WAY TOO heavy." 
print "He`s got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print " If I add %d, %d, and %d I get %d. " % (my_age, my_height, my_weight, my_age + my_height, + my_weight)

# This issue I was haveing running this script is explained in Exercise 6. 
# I get error TypeError: not all arguments converted during string formatting. 
"""
	You need to make sure that the line of code is exactly the same. What happens in this error is you have more % format characters in the string than variables to put in them. Go back and figure out what you did wrong. 
"""