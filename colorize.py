class Color:
    def __init__(self, _c):
        self.color = _c

    def __dir__(self):
        return ['r', 'c', 'g', 'b', 'y', 'k', 'w', 'None', 'all x']

    def set_color(self):
        from colorama import Fore, Style
        if self.color == 'r':
            return Fore.RED
        elif self.color == 'rx':
            return Fore.LIGHTRED_EX
        elif self.color == 'm':
            return Fore.MAGENTA
        elif self.color == 'mx':
            return Fore.LIGHTMAGENTA_EX
        elif self.color == 'c':
            return Fore.CYAN
        elif self.color == 'cx':
            return Fore.LIGHTCYAN_EX
        elif self.color == 'g':
            return Fore.GREEN
        elif self.color == 'gx':
            return Fore.LIGHTGREEN_EX
        elif self.color == 'b':
            return Fore.BLUE
        elif self.color == 'bx':
            return Fore.LIGHTBLUE_EX
        elif self.color == 'y':
            return Fore.YELLOW
        elif self.color == 'yx':
            return Fore.LIGHTYELLOW_EX
        elif self.color == 'k':
            return Fore.BLACK
        elif self.color == 'kx':
            return Fore.LIGHTBLACK_EX
        elif self.color == 'w':
            return Fore.WHITE
        elif self.color == 'wx':
            return Fore.LIGHTWHITE_EX
        else:
            return Style.RESET_ALL
