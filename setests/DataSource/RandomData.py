__author__ = 'LFawzy'
import random, string
from random import randint


class RandomGeneration:
    def random_string(length):
        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))

    def random_password(length):
        characters = ''.join(random.choice( string.ascii_lowercase+string.ascii_uppercase) for i in range(length))

        digits = ''.join(random.choice( string.digits) for i in range(length))
        return characters+digits

    def random_email(length):
        letters = string.ascii_letters
        domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
        random_letter = ''.join(random.choice(letters) for i in range(length))
        random_domain = random.choice(domains)
        return random_letter + '@' + random_domain


    # randint(1000,2000)
