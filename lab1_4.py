def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3)/3 
#calculates avg of 3 numbers

def add_tax(bill_total):
    return bill_total * 1.1
#calculates a 10% tip

def greet_user(name):
    return "Hello " + name
#greets user

assert(calculate_average(3, 4, 5), 4)
assert(add_tax(10), 11)
assert(greet_user("Ethan"), "Hello Ethan")