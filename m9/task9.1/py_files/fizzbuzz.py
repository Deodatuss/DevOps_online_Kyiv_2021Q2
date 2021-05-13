def get_reply(number):
    if (not number % 5) and (not number % 3):
        return 'FizzBuzz'
    elif not number % 3:
        return 'Fizz'
    elif not number % 5:
        return 'Buzz'
    else:
        return f'{number}'
