'''Extracting numbers.

Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.

Constraint: use only while loop for iteration.'''


int_list =[]
special_int = 1

while len(int_list)<=100:
	int_list.append(special_int)
	special_int += 1

new_list =[]

for i in int_list:

	if i%7 ==0 and i % 5 !=0:
		new_list.append(i)

print(new_list)
