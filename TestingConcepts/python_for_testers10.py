"""
Variable scope in python - boundary of variables within a program
1. Local Variable
2. Global Variable
3. Global Keyword
4. LEGB rule: Local -> Enclosing -> global -> Built-in
"""

print("-----------------Local Variable Scope-------------------")
def localvar():
    x = 10
    print(x, "Locally accessible - inside method localvar")

def anothermet():
    print(x, "Not accessible - because x is not present locally tho anothermet")

localvar()
# anothermet()    # Throws an error

print("-----------------Global Variable Scope-------------------")
x = 10
def localvar():
    print(x, "accessible - because it is a global variable")

def anothermet():
    print(x, "accessible - because it is a global variable")

localvar()
anothermet()

print("-----------------Global Keyword-------------------")

def localvar():
# Even though if we declare x locally. it will be accessible in any method because we declared global keyword.
    global x
    x = 10
    print(x, "accessible - because it is a global variable")

def anothermet():
    print(x, "accessible - because it is a global variable")

localvar()
anothermet()

print("-----------------Enclosing Scope-------------------")

x = 10
def grandparentmet():
    x = 50
    print(x)
    def parentmet():
        x = 70
        print(x)
        def childmet1():
            print(x)
        childmet1()
    parentmet()
grandparentmet()

