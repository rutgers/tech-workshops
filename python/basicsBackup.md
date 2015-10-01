# Rutgers IEEE Student Branch - Python Basics Workshop

## Workshop Leaders

Ravi Bhankharia, Niral Shah

## Module 0 - What is Python?

Python is a powerful, popular, general-purpose programming language.

Some important facts about python:

* **Python is dynamically typed.** This means that a variable can be an int, string, double, etc., without being declared as such.
* **Python is white-space delimited.** This means that there are no `{ curly brackets }` surrounding blocks of code, rather blocks are indicated by their indentation level (we will show examples of this later).
* **Python is an interpreted scripting language.** This means that Python should run identically on different operating systems, you don't compile Python programs, and additionally that Python scripts can help automate tasks.

## Module 1 - Basic Syntax

### A. Input/Output

Here's an example of a simple Python Hello World program:

```python
# Hello World Program!
# <- Octothorpes indicate comments.

a_variable = "Hello World!"
print(a_variable)
```

Notice here that there is no set type for `a_variable`. We could have put `a_variable = 42` at the end and Python would be totally okay with that. And while this allows for flexibility, it can also lead to hard-to-detect errors. So be careful!

To take user input, another relatively common task, use the `input("some prompt")` function. Here's another example:

```python
# An example of input.

user_name = input("What is your name? ")
user_age = input("What is your age? ")

print("So you are " + user_name + " and you are " + user_age + " years old.")
print("Nice to meet ya!")
```

Notice how the input function (in python 3) was used. It takes whatever the user inputs and converts it to a string. This is good because `print` can only put together strings.

How do you run/wrote these programs? If you are on a Mac or Linux, you can go to the terminal, change your directory to where your program is stored, and type in the command `python your_program.py`. You can write these programs in most text editors, just remember to save it as a `.py` extension!

On Windows, you can write a program in IDLE by going to File, New File. From that editor you can run your program by going to Run, Run Module.

### B. Loops and Conditionals

An important feature of any language is loops and if/else logic! So to explain how to use them, here's an example of a **while loop**:

```python
# Loops

print("Here's a question for you: ")
guess = input("How many lines would it take to write this program in Java? ")

while(guess.strip().lower() != "too many"):
print("Not quite...")
guess = input("Try again! ")
print("You got it!")
```

Some important things to notice here are the colon after the while loop condition, and the indented lines following. The indentations represent the statements within the while loop block, and this helps force more readable code. And though tabs are preferable, any amount of whitespace will do, even a single space (though that would make your code much more difficult to read).

Also in this program, the `strip` function gets rid of trailing spaces (including the newline), and the `lower` function converts the string to lowercase.

Here is a quick for loop example:

```python
for i in range(0,10):
print(i)
```

For loops look a little different, because they iterate through a list directly. The range method creates a list (which we will cover soon) of the numbers 0 to 9. But this can work for any list, making for loops very useful.

**Conditional Statements:** The keywords in Python are if, elif, and else. They also terminate with a colon (`:`) and use whitespace for their blocks. This looks something like:

```python
# Simple guessing game

print("I'm thinking of a number from 1 to 10, can you guess it?")
while(True):
guess = input("Your Guess: ")
if guess.isdigit():
guess = int(guess)
else:
print("Nope")
continue
    
if guess == 4:
print("Correct!")
break
elif guess > 4:
print("Too high.")
else:
print("Too low.")
```

The continue statement skips the rest of the loop and starts it over. The `isdigit` function checks if guess is an int, and the `int` function converts guess to an integer.
  

### C. Lists/Arrays and Dicts

Lists are Python's arrays, and come with a handful of useful built-in functions to manipulate them. Here's what a list looks like:

```python
mylist = [2, "string", 3.3]
```

They can contain different types as well. Let's talk about slice notation - lists can be cut into smaller lists by using brackets after the list. Using the given list above, typing in

```python
print mylist[1:2]
```

prints from the second element (python lists start from index 0) to the third element. If you don't include a number after the colon (`mylist[1:]`, it prints from the second element to the end of the list. `mylist[:1]` will print everything from the beginning of the list to the second element. Strings in Python can be manipulated the same way.

Dictionaries in Python are similar to hash tables if any of you have taken Data Structures. It maps a bunch of 'keys' to a bunch of 'values'. Keys are unique, but values can be anything. You can get the value by feeding in a key to the dict in the following manner:

```python
mydict = {'hello' : 1, 'world' : 2}
mydict['hello'] # returns 1
mydict['world'] # returns 2
```

### D. Functions

Show how to make a function using def

Functions in python use the def keyword.

```python
def myFunction(myArgument, anotherArg):
print("in myFunction")
return 2
```

The return statement lets you send back information, like `info = myFunction(1,2)`.

## Module 2 - Guessing Game

Create a guessing game where you ask the user for integers and print 'higher' or 'lower' depending on their input. Give them 5 tries to guess it properly before exiting. We'll help you out if you hit any roadblocks.



## Module - References

http://www.astro.ufl.edu/~warner/prog/python.html

https://en.wikipedia.org/wiki/Python_%28programming_language%29
