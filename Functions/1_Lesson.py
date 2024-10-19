# What are functions

#  Its a module
# How to create a function

# def name_of_function(parameters / arguments (optional)):
    # write here whatever you want your function to do 
    # print something
    # adding two numbers

# Functions are of 2 types
# Built in function ( input() or print())
# User defined function


# ===================Functions without arguments ==================
def show_number():
    x = 8
    print(x)

def greet():
    print("Welcome")


# calling
show_number()
greet()


# ===================Functions with arguments ==================
def greet(name):
    print("Welcome: ", name)


greet("Maxim")
greet("Fiza")
show_number()

def show_number(x):
    print(x)



show_number(3)
show_number(4)

# ======================Function to add two numbers ============================

def add_numbers(y , z):
    print("sum of ",y, " and ", z, " is: ", y+z)

add_numbers(5,9)

# Add 2 nums and mul with 5

add_numbers(2,3)


# ====================== The return statement =================================
def add_numbers(y , z):
    return y+z


result= add_numbers(9 ,6)
# print("sum of 9 and 6 is: ", result)
print("Multiply by 5 ", result*5)



# ==================Square of a function =======================

def find_square(num):
    result = num*num
    return result

square  = find_square(8)
print("Square: ", square)



def subtract():
    pass

def divide():
    pass
 
def product():
    pass



# ==================More arguments=================

# Function to add two lists
def add_list(list1 , list2):
    pass


x = [23, 78 , 90]
y = [8,9,10]

add_list(x,y)