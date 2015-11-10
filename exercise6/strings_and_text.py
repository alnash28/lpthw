# Exercise 6 Strings and Text

# While you have alreadu been writing stings, you still do not know what they do. 
# In this exercise, we create a bunch of complex strings so you can see what they are for. 
# We will now type in a whole bunch of strings, variables, and formats, and print them. You will
# also practice using short abbreviated variable names. Programmers love saving themselves time at 
# your expense by using cryptic variable names, so let`s get you started being able to read and write
# them early on 

x = " There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x 
print y 

print "I said: %r."  % x 
print "I also said: '%s'. " % y 

hilarious = False 
joke_evaluation = "Isn`t that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e 