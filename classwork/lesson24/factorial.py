
def factorial_1(number):
    result_product = 1
    while number > 0:
        result_product *= number
        number -= 1
    return result_product


print(factorial_1(4))


# recursive approach
def factorial_2(num):
    if num <= 1:
        return 1
    else:
        return num * factorial_2(num-1)


print(factorial_2(5))
