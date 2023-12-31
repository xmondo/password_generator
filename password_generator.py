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
        print()
        for k in range(0, self.quantity):
            ri_1 = random.randint(self.lower_limit, self.upper_limit)
            ri_2 = random.randint(self.lower_limit, self.upper_limit)
            pw = (rw.get_random_word().capitalize() + '-' + str(ri_1) + '-' + rw.get_random_word().capitalize() +
                  '-' + str(ri_2) + '-' + rw.get_random_word().capitalize())
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


if __name__ == '__main__':
    try:
        RandomCombo(5, 1999999, 9999999).word_integer_combination()
        RandomString(5, 64).random_secret()
    except Exception as err:
        print(err)
