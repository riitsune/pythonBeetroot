'''User could input to you something. You'll to transform it 
to int and divide 1 by this number. Don't use if/else blocks 
and print "Wrong input" in case if some exception happen'''


user_input = input("please enter some number")

new_int = int(user_input)
try:
	1/new_int
except print(ValueError, e):
	print("Wrong input, please type number")
  
