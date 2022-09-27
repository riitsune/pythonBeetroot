'''Task 1

Make a program that has some sentence (a string) on input 
and returns a dict containing all unique words as keys and the number of occurrences as values. '''




my_dictionary = {}

for word in keys:
    if word in my_dictionary:
        my_dictionary[word] += 1
    else: 
        my_dictionary[word] = 1

print(my_dictionary)
