'''Write a program, which has two print statements to print the following text (capital letters "O" and "H", made from "#" symbols):'''


a="#########"
b="#\t\t#"

letters = [a,b,b,b,a]
also_letters =[b,b,a,b,b]
for x in letters:
    print(x, end = '\n')

for i in also_letters:
    print(i)
