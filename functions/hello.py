def hello():
    return "Hello, World!"
# print(hello()) #function call

def greeting(name):
    return f"Hello, World, my name is {name}"
# print(greeting("Alice"))
# print(greeting("Noriss"))
# print(greeting("Hamilton"))
# print(greeting()) #error missing positional argument

def sum():
    a = 5
    b = 10
    return a + b
# print(sum())

def sum(a, b):
    return a + b
# print(sum(5, 10))
# print(sum(3, 7))
# print(sum(9, 7.5))

def concatenate(str1, str2, str3):
    return f"{str1} {str2} {str3}"
# print(concatenate("Hello","World"))
# print(concatenate("Good", "Morning"))
print(concatenate("My name is john doe, I am a computer science student.", "I love programming.", "I am currently learning python."))
