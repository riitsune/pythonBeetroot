'''Task 2

Creating a dictionary.

Create a function called make_country, which takes in a country’s name and capital as parameters. 
Then create a dictionary from those parameters, with ‘name’ and ‘capital’ as keys.
Make the function print out the values of the dictionary to make sure that it works as intended.'''


def make_country(country, capital):
    country_dict ={'Country':country, "Capital": capital}
    return country_dict


country_name = input("Type here name of a country\n")
capital_name = input("Type here country's capital\n")


print(make_country(country_name, capital_name))
