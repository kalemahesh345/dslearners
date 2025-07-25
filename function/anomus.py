# Anomus function is a single expretion functons........

# square = lambda x:x*x
# print(square(10))




# def func(num):
#     n1,n2=0,1
#     print(n1,n2,end=" ")
#     for i in range(2,num):
#       n3=n1+n2
#       n1=n2
#       n2=n3
#       print(n3, end=" ")

# num=int(input("Enter the number: "))

# func(num)


# def func(num=14):

#     steps=0
#     while num > 0:


    
#          if num % 2==0:
#           num = num//2

#          else:
#           num = num - 1
#          steps +=1
#     return(steps)

# 1. Defoult Argument..............

# def default(name="mahi"):
#     print("hello "+name + " well come to DreamsGuider")

# default()
# default("shubham")



# 2.key world Arguments......

# def display(name, age):
#     print(name + " is " + str(age) +" yaers old")
# display(age=21, name="mahesh")


# 3.Required [possitiona ] argument...........
# def multiple(x, y):
#     return x * y
# print(multiple(2 ,5))

#  * is select all argument in function.....

# def total(*number):
#     sum=0

#     for num in number:
#         sum +=num
#     print("sum: ",sum)
# total(1, 2, 3, 4)


# **is used to key words keyword variable-length argument.........

# def show_details(**info):
#     for key, value in info.items():
#         print(f"{key}: {value}")

# show_details(name="mahi", age=21, city="Newasa")


# write a function that return the largest number in a list.......

def large(*num):
    print("this is a max number:",max(num))
    
large(10,20,44,5,14,85,97,64,48,54)
