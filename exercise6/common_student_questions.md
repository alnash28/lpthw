
# What are the difference between %r and %s? 

	```
	We use %r for debugging, since it displays the "raw" data of the variable, but we use %s 
	and others for displaying to users

	```
# I get error TypeError: not all arguments converted during string formatting. 

	```
	You need to make sure that the line of code is exactly the same. What happens in this error is you have more % format characters in the string than variables to put in them. Go back and figure out what you did wrong. 

	```	
    ```python 
    Traceback (most recent call last):
    File "../exercise5/more_variables_and_printing.py", line 23, in <module>
    print " If I add %d, %d, and %d I get %d. " % (my_age, my_height, my_weight, my_age + my_height, + my_weight)
    TypeError: not all arguments converted during string formatting
    ```