'''User could input to you something. You'll to transform it 
to int and divide 1 by this number. Don't use if/else blocks 
and print "Wrong input" in case if some exception happen'''


user_input = input("please enter some number")

new_int = int(user_input)
try:
	1/new_int
except print(ValueError, e):
	print("Wrong input, please type number")
	
	
#second way	
user_input = input("Enter your value: ")

def some_function (argument):
    try:
        user_input_int = int(user_input)
        return 1/user_input_int
    except ValueError:
        print("Your input is incorrect, use an int")
    except ZeroDivisionError:
        print("You cannot divide on zero, try another number")

print(some_function(user_input))
  
