# Python

* Launch the IDLE program to run your python
* You can enter single commands directly at the prompt.
* Python files end in `.py`. You can write Python programs in these files. These can have multiple commands on after the other.

## Numbers
* A normal number is called an integer in programming. This is sometimes called int for short.
* Arithmetic is another work for maths and Python supports a number of arithemetic operations e.g. + is plus, - is minus, * is multiply and / is divide.
* You can type arithmetic expressions directly at the command prompt and it will give you the result

## Strings
* A string is a sequence of characters. These can be words or sentences. If you are typing it in to the program file you should surround it by quotes e.g. `"hello"` or `"noob"` or `"."` or `"7"`.
* You can join strings together using `+` e.g. `"hello" + " " + " noob"`
* To convert something to a string you use `str()` e.g. to convert `10` to `"10"` you use `str(10)`

## Print
* To print you use `print()` and the thing you want to print goes in between the brackets.
* You can print strings directly by typing them in with quotes e.g. `print("hello world")`
* You can print out a number by putting it in between the brackets. If you are printing a single number it doesn't matter if you use quotes or not.
	* If you print a number expression with quotes then it will print whatever is on the screen exactly. `print("7+3")` will print out `7+3`.
 	* If you don't have the quotes it will do whatever arithmetic operation first and only print out the result. `print(7+3)` will print out `10`
* To join things together and print them you can use `+` but both sides of the plus must be a string.

## Variables

* A variable is a place to store a piece of information. This can store an integer or a string or any other expression.
* A variable has a name which can be used later to refer to the variable
* A variable has a type which tells us what is stored in the variable e.g. integer, string
* A variable has a value which is the thing stored in the variable. The value can be changed to another value later.
* We use the `=`sign to store something in a variable e.g. `davids_age = 7`. After this the variable has the value 7.
* You can change the value stored in a variable by putting a new value in there e.g. after `davids_age = 8`, now the variable has the value 8.

## Input

* To ask the user a question we use the `input` function. This will print out a question to the screen, get the response from the user and put it in a variable.
* For example `name = input("What is your name? ")`. Whatever the user types in will be stored in the variable called `name`.
* The `input` function returns a string. Even if the user types in a number it will be stored as a string variable.

## Lists



## Errors

* `TypeError: 'str' object is not callable` - You forgot a plus between two strings and the second string has brackets around it.
* `Syntax Error` - for strings maybe you forgot a plus somewhere
* `TypeError: 'NoneType' object is not callable` - You have an extra closing bracket `)` in the middle of the string
* `TypeError: can only concatentate str (not "list") to str` - You can only join a string to a string. You are missing a call to `str` for one of the variables you are printing
