import random
import string


def string_reverser(input_string):
    """
    Reverse all input string
    :param input_string:
    :return: reversed data
    """
    reverse_string = input_string[::-1]
    return reverse_string


def random_number_generator(size=10, chars=string.ascii_uppercase + string.digits):
    """
    Random number generator.
    :param size:
    :param chars:
    :return:
    """
    random_number = ''.join(random.choice(chars) for _ in range(size))
    return random_number
