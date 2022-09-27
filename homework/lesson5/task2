
'''Task 2

Exclusive common numbers.

Generate 2 lists with the length of 10 with random integers from 1 to 10, 
and make a third list containing the common integers
 between the 2 initial lists without any duplicates.

Constraints: use only while loop and random module to generate numbers'''

import random

rand_list1 =[]
rand_list2 =[]
n1=1
n2=n1
list_length = 10
while n1<= list_length:
	rand_list1.append(random.randint(1,10))
	rand_list2.append(random.randint(1,10))
	n1 += 1
same_list = []
i=0
while i<len(rand_list1):
	if rand_list1[i] in rand_list2:
		same_list.append(rand_list1[i])
		i += 1
print(rand_list1,rand_list2)
print(same_list)
