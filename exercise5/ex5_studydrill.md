
# Exercise 5 Study Drill 

1. Change all the variables so there isnt the my_ in front. Make sure you change the name everywhere, not just where you used = to set them 

```python 

age = 29 # Not a lie 
height = 71 # inches 
weight = 270 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Lets talk about %s." % name
print "He`s %d inches tall." % height
print "He`s %d pounds heavy." % weight
print "Actually that`s WAY TOO heavy." 
print "He`s got %s eyes and %s hair." % ( eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print " If I add %d, %d, and %d I get %d. " % (age, height, weight, age + height, + weight)

``` 

2. Try more format characters. %r is a very useful one. It`s like saying "print this no matter what."



3. Search online for all the Python format characters. 

src: https://docs.python.org/2/library/stdtypes.html#id16

|Conversion |Meaning Notes|
|-----------|-------------|
|'d'|Signed integer decimal.|	 
|'i'|Signed integer decimal.|	 
|'o'|Signed octal value.|
|'u'|Obsolete type – it is identical to 'd'.|
'x'	Signed hexadecimal (lowercase).	(2)
'X'	Signed hexadecimal (uppercase).	(2)
'e'	Floating point exponential format (lowercase).	(3)
'E'	Floating point exponential format (uppercase).	(3)
'f'	Floating point decimal format.	(3)
'F'	Floating point decimal format.	(3)
'g'	Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
'G'	Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.	(4)
'c'	Single character (accepts integer or single character string).	 
'r'	String (converts any Python object using repr()).	(5)
's'	String (converts any Python object using str()).	(6)
'%'	No argument is converted, results in a '%' character in the result.	 


4. Try to write some variables that convert the inches and pounds to centimeters and kilos. Do not just 