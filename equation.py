# solve the equation ax^2 + bx + c = 0
# delta = b^2 - 4ac
# if delta < 0 No solution
# if delta = 0
# if delta > 0
# input a
import math


# function to get the number from the input, q to quit,
def get_input():
    user_data = input("please enter parameters as a real number, or 'q' to quit")
    if user_data == 'q':
        return exit()
    try:
        user_number = float(user_data)
        return user_number
    except ValueError:
        print("I need a number to continue")
        return get_input()


a = get_input()
print(f"you have a equal: {a}")
# input b
b = get_input()
print(f"you have b equal: {b}")
# input c
c = get_input()
print(f"you have c equal: {c}")
# calculate delta:
delta = b ** - 4 * a * c

# if delta < 0
if delta < 0:
    print("No solutions\n")
elif delta == 0:
    print(f"equation has solution: {-b / 2 * a}")
else:
    print(f"equation has the first solution is: {(-b + math.sqrt(delta))} \n")
    print(f"equation has the first solution is: {(-b - math.sqrt(delta))} \n")
