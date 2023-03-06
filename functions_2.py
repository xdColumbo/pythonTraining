a = 10
b = 20


def addition1():
    print(a + b)


def addition2(a, b, c=4):
    return a + b + c


def addition3(*args):  # the args can be named anything after the * char
    return sum(args)


def greetings(*args):
    greeting = "there are so many ways to say hello : "
    for g in args:
        greeting += g
        greeting += ", "
    print(greeting[0:len(greeting)-2])


greetings("Hi", "Hello", "Good morning", "Bye", "Nice to see you")

addition1()
amount = addition2(45, 25)
print(amount)

print(addition3(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
