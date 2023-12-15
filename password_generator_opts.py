class RandomCombo:
    def __init__(self, quantity, lower_limit, upper_limit):
        self.quantity = quantity
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def word_integer_combination(self):
        import random
        from random_word import RandomWords
        import colorize as clr
        blu = clr.Color('bx').set_color()
        reset = clr.Color(None).set_color()
        rw = RandomWords()
        random_characters = ['@', '#', '$', '%', '&', '!']
        print()
        for k in range(0, self.quantity):
            ri1 = random.randint(self.lower_limit, self.upper_limit)
            rc1 = str(ri1) + str(random.choice(random_characters)) + str(random.choice(random_characters))
            ri2 = random.randint(self.lower_limit, self.upper_limit)
            rc2 = str(random.choice(random_characters)) + str(ri2) + str(random.choice(random_characters))
            pw = (rw.get_random_word().capitalize() + '-' + str(rc1) + '-' + rw.get_random_word().capitalize() +
                  '-' + str(rc2) + '-' + rw.get_random_word().capitalize())
            print(blu + pw + reset)
        return print()


class RandomString:
    def __init__(self, quantity, length):
        self.quantity = quantity
        self.length = length

    def random_secret(self):
        import secrets
        import colorize as clr
        red = clr.Color('rx').set_color()
        reset = clr.Color(None).set_color()

        count = 0
        while count != self.quantity:
            charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&'
            passwd_string = ''.join(secrets.choice(charset) for _ in range(self.length))
            print(red + passwd_string + reset)
            count += 1
        return print()


class GetInputs:
    @staticmethod
    def commandline_options():
        import argparse
        import sys
        parser = argparse.ArgumentParser()
        parser.add_argument("number_of_passwords", type=int, help="number of passwords")
        parser.add_argument("lower_limit", type=int, help="lower limit")
        parser.add_argument("upper_limit", type=int, help="upper limit")
        parser.add_argument("random_string_length", type=int, help="random string length")
        args = parser.parse_args()
        number_of_passwords = args.number_of_passwords
        lower_limit = args.lower_limit
        upper_limit = args.upper_limit
        random_string_length = args.random_string_length

        if lower_limit > upper_limit:
            print('lower limit must be less than upper limit')
            # exit error 2: misuse of shell command
            sys.exit(2)
        else:
            return number_of_passwords, lower_limit, upper_limit, random_string_length


if __name__ == '__main__':

    try:
        q, ll, ul, rl = GetInputs.commandline_options()
        RandomCombo(q, ll, ul).word_integer_combination()
        RandomString(q, rl).random_secret()
    except Exception as err:
        print(err)

