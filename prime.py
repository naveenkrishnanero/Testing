def is_prime(number):
    """ return True if number is prime """
    for i in range(2,number):
        if (number%i==0):
            return False
    else :
        return True


def print_next_prime(number):
    """ return the next prime number """
    while True:
        number +=1
        if (is_prime(number) is True):
            print number
            break


