#use numpy to have a nonstandard step
import numpy

def get_input():
    user_data = input("please input a number, or 'q' for exit \n")
    if user_data == 'q':
        exit()
    try:
        user_data = float(user_data)
        return user_data
    except ValueError:
        print("your input is not a number, give me a number, please \n")
        return get_input()

#get the input from user
print("please give me the fisrt parameter a:\n")
a = get_input()
print("Please give me the second parameter b:\n")
b = get_input()
print("Please give me the third parameter c:\n")
c = get_input()
#for each of x in the step, print y if y value is around 0
for x in numpy.arange(-50,50,0.1):
    y = a*x**2 + b*x + c
    if (-0.01<y<0.01):
        print(x)
    else:
#        print("**\n")
        pass


