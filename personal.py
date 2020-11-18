def title(string, rng, color=0):
    """
    --> Function to create a title in the project.
    :param string: Written part of the title.
    :param rng: Title range.
    :param color: Title color. (30 = White; 31 = Red;    32 = Green; 33 = Yellow;
                                34 = Blue;  35 = Purple; 36 = Cyan;  37 = Grey)
    :return: Nothing.
    """
    print(f'\033[{color}m-' * rng)
    print(f'{string:^{rng}}')
    print(f'\033[{color}m-\033[m' * rng)


def inputInt(string=''):
    """
    --> Function to read a int number.
    :param string: Written part.
    :return: The int number.
    """
    a = input(string)
    while True:
        try:
            int(a)
        except ValueError:
            a = input(f'\033[31m[ERROR]\033[m {string}')
        except KeyboardInterrupt:
            print('The user chooses not to provide all data.')
            return 0
        else:
            break
    return int(a)


def inputFloat(string=''):
    """
    --> Function to read a float number.
    :param string: Written part.
    :return: The float number.
    """
    a = input(string)
    while True:
        a = a.replace(',', '.')
        try:
            float(a)
        except ValueError:
            a = input(f'\033[31m[ERROR]\033[m {string}')
        except KeyboardInterrupt:
            print('The user chooses not to provide all data.')
            return 0
        else:
            break
    return float(a)


def inputName(string=''):
    """
    --> Function to read a person's name.
    :param string: Written part.
    :return: The name.
    """
    a = input(string)
    while not a.replace(' ', '').isalpha():
        a = input(f'\033[31m[ERROR]\033[m {string}')
    return a.title().strip()


def menu(lst, ttl='MENU', rng=50, color=0):
    """
    --> Function to create a menu in the program.
    :param lst: List with the options.
    :param ttl: Title.
    :param rng: Title range.
    :param color: Title color. (30 = White; 31 = Red;    32 = Green; 33 = Yellow;
                                34 = Blue;  35 = Purple; 36 = Cyan;  37 = Grey)
    :return: Nothing
    """
    title(ttl, rng, color)
    c = 1
    for items in lst:
        print(f'\033[33m{c} - \033[34m{items}\033[m')
        c += 1
    print(f'\033[{color}m-\033[m'*rng)


def readArch(name):
    """
    --> Function to read a .txt archive.
    :param name: Archive name.
    :return: Nothing.
    """
    try:
        a = open(name, 'rt')
    except FileNotFoundError:
        print('\033[31mArchive not found!\033[m')
    else:
        print(a.read())
        a.close()
