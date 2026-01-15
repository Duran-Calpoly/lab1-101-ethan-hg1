def check_multiple(number):
    if number % 3 == 0 and number % 5 == 0:
        return True #number is multiple of 3 and 5
    else:
        return False #number is not either
    
def check_password(input_string):
    input_string = "Python123"
    if input("password: ") == input_string:
        return("access granted") #matches string
    else:
        return("access denied") #does not match string
    
def calculate_federal_tax(salary):
    if salary >= 11000:
        if salary >= 44725:
            if salary >= 95375:
                return salary * .24 #highest bracket 
            return salary * .22 #second highest bracket
        return salary * .12 #third highest bracket
    else:
        return salary * .1 #lowest bracket
                