#function 1.................,function is block of code that is perform specific task of code
#      syntax 
#             def_function_name(parameter)
#                    """ docstring """
#              statment(s)
#              return expretion

# 1..
# def addnum(a,b,d):
#     c=a+b+d
#     print(c)
# addnum(2,3,5)
# addnum(5,4,2)


# 2...
# def greet(name,age):
#     print(f"Hi,I am {name},and i am {age} year of old.")   # f is possitnal variable....

# greet("mahesh", 21)


# 3. local varible...

x = 10
def func():
    x = 5
    print("local x:",x)  # this is local variable ..

func()
print("Global x: ",x)    #this is Global variable..



# 4. scope and lifetime..

x = 10 

def func():
    x = 5
    print(x)



