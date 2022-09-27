'''The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. 
The program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.'''

phone_num = input("put your phone number here: ")


if phone_num.isdigit() is False:
    print("try to put only numbers!")
elif len(phone_num)!=10:
    print("error! Too less or too many numbers")

else :
    print("Thank you for giving your number hahahha")
