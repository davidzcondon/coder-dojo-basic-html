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

* A list can contain a number of items (or elements). There is no limit to the number of items (unless you run out of memory).
* You can have an empty list e.g. `transformers = []`
* You can create a list using `transformers = ["Megatron", "Optimus Prime", "Soundwave", "Thundercracker"]`
* You can get the length of the list using the `len` function e.g. `number_transformers = len(transformers)`
* List numbering starts from 0 so to get the first item in a list you use `first = transformers[0]`. You can get the 3rd item of a list using `transformers[2]`.
* If you try to get an index in the list that is larger than the size of the list you get a `list index out of range error`.
* To change an item in the list you use the index and assign a new value to it e.g. `transformer[1] = "unicron"`

## Loops

* If we want to do something to every item in a list we must "loop" over the list
* One type of loop is the `for` loop. To loop over every item in a `devices` list we do 
```
for device in devices:
    print (device)    ## <--- This is the loop body 
```
* This will go through the list and put the current item in the `device` variable. It will start at the first item in the list. It will run the code in the loop body using that value of device. Then it will move onto the next item in the list and run the loop body until all the items in the list have been used.

## Object

* An object is a more complicated type than an integer or string
* It has lots of `attributes` or `properties`
* You can call `methods` on an object to get it to do something e.g. return its name or update one of its attributes.
* If we had an object called `david` and it had a property called `name`, we could use this in our code with `david.name`
* `None` is a special object. Any variable can be set to `None`. It means that the obejct is empty.

## Conditionals

* This allows you do do something if based on whether thing is true or false.
* You can compare two items using `==`. If are the same it evaluates as `True`. If they are different it evaluates as `False`.
* The format of a basic if statement is
```
if device.name == "test":
    print (device.name)    ## <--- This will only be executed if the condition in the previous line is True
```
* If we want to do something when the conditional is False we use an `else` statement
```
    if device.name == "Microsoft X-Box 360 pad":
        print("We found an X-Box controller. Using this!") # <-- If it condition is True we come in here
        xbox_controller = device
    else:
        print("Found " + device.name + ". Skipping!") # <-- If it condition is False we come in here
```
* Only one of the `if` or `else` block will be executed at any one time. Both can't be executed for the same condition.

## Libraries

* We can use other people's code in our programs. They give their code to us in libraries.
* We can install the library on our system using `pip install library-name`.
* To use the library in our code we can use `import library-name` for the whole library
* Or for a part of the library we can use `from library-name import component-name`

## Errors

* `TypeError: 'str' object is not callable` - You forgot a plus between two strings and the second string has brackets around it.
* `Syntax Error` - for strings maybe you forgot a plus somewhere
* `TypeError: 'NoneType' object is not callable` - You have an extra closing bracket `)` in the middle of the string
* `TypeError: can only concatentate str (not "list") to str` - You can only join a string to a string. You are missing a call to `str` for one of the variables you are printing
* `list index out of range error`. You tried to access an item in the list that isn't there e.g. access the sixth element of a list which only contains three elements.
* `NameError: name 'something' is not defined`. The variable `something` is not defined. Either you forgot to define it or you meant it to be a string and you forgot the quotes around the string

## Terminal

* This is where we can run our programs.
* When we open the terminal we start in a folder.
* Some commands
    * `ls` shows the contents of the current folder.
    * `cd folder-name` moves us into the folder named folder-name. `cd ..` moves us up a folder.
    * To create a new folder use the `mkdir folder-name` command.
    * Use `python program.py` to run the program in the `program.py` file
* The terminal is case-sensititve. That means that the capital letters matter so that a folder named `music` is different from a folder named `Music`
* The terminal does auto complete for filenames. Pressing tab will complete the name if it can.
* You can use the `up arrow` and `down arrow` to go through the previous commands.
