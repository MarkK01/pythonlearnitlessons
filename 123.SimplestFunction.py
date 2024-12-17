def say_hi():
    print("Hello there!")
    print("goodbye")
say_hi()

def three_3_function():
    print(33)
three_3_function

# Default Argument
def yell_this(phrase = "good night"):
    print(phrase.upper() + "!")
yell_this("good morning")
yell_this()

# Function Return Value
def msg_double(phrase):
    double = phrase + " " + phrase
    return double
msg_2x = msg_double("let's go")
print(msg_2x)

def half_value(value):
    return value/2
print(half_value(42))