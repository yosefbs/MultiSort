import random
import string


def get_random_text():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    return x
