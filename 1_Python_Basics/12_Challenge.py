def fizz_buzz(num):
    if(num % 3 == 0 and num % 5 == 0):
        return 'FIZZ_BUZZ'

    if(num % 3 == 0):
        return 'FIZZ'
    if (num % 5 == 0):
        return 'BUZZ'
    return num


print(fizz_buzz(3))
