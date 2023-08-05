class RandomCombo:
    def __init__(self, quantity, lower_limit, upper_limit):
        self.quantity = quantity
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def word_integer_combination(self):
        import random
        from random_word import RandomWords
        rw = RandomWords()
        print()
        for k in range(0, self.quantity):
            ni = random.randint(self.lower_limit, self.upper_limit)
            pw = rw.get_random_word().capitalize() + '-' + str(ni) + '-' + rw.get_random_word().capitalize() + '-' + rw.get_random_word().capitalize()
            print(pw)
        return print()


class RandomString:
    def __init__(self, quantity, length):
        self.quantity = quantity
        self.length = length

    def random_secret(self):
        import secrets
        count = 0
        while count != self.quantity:
            charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&'
            print(''.join(secrets.choice(charset) for _ in range(self.length)))
            count += 1
        return print()


if __name__ == '__main__':
    try:
        RandomCombo(5, 19999, 99999).word_integer_combination()
        RandomString(5, 64).random_secret()
    except Exception as err:
        print(err)
