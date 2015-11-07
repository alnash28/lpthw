# Exercise 3 Study Drill 

1. Above each line, use the # to write a comment to yourself explaining what the line does. 

2. Remember in Exercise 0 when you started Python? Start Python this way again and, using the above characters 
and what you know, use Python as a calculator.

3. Find something you need to calculate and write a new .py file that does it. 

``` 
See attached 'ex3.3_calculate.py' 

```

4. Notice the math seems "wrong"? There are no fractions, only whole numbers. Find out why by reasearching what a "floating point" number is. 

```
A "floating point" number, also called floats, represent real numbers and 
are written with a decimal point dividing the integer and fractional parts. 

``` 

5. Rewrite ex3.py to use floating point numbers so its`s more accurate (hint 2.0 is floating point).

```python 

print " I will now count my chickens:"

print "Hens", 25.0 + 30.0/6.0 
print "Roosters", 100.0 -25.0 * 3.0 % 4.0

print "Now I will count the eggs"

print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

print "Is it true that 3.0 + 2.0 < 5.0 - 7.0 ?"

print  3.0 + 2.0 < 5.0 - 7.0 

print "What is 3.0 + 2.0?", 3.0 + 2.0 
print "What is  5.0 - 7.0?" , 5.0 - 7.0

print "Oh, that`s why it`s False."
 
print"How about some more." 

print "Is it greater", 5.0 > -2.0
print "Is it greater or equal?", 5.0 >= -2.0 
print "Is it less or equal?", 5.0 <= -2.0

```