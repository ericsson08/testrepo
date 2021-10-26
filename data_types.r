# Data Types
The first three data types you will need to start using R are

numeric
character
logicals

Numeric
In general, numeric data types include negative and positive numbers. These include decimal valued numbers as well. For example, each of the below is an example of a numeric value:

5 # this is numeric
5.3 # this is numeric
-12 # this is numeric
-1.2 # this is numeric

Character
Another data type is a character. Characters are either defined with ' or " quotes around a set of text.

"This is a character" # this is a character
'This is a character' # this is a character
'This is a character" # this is an error - both start and end must match
Logical
Logicals in R must be in all caps. They are the values TRUE and FALSE.

TRUE # this is a logical
True # this is not a logical
In order to know what data type something is in R, we can use the keyword class.

class(TRUE) # returns 'logical'
