
#!/usr/bin/env python3

# -*- coding: utf-8 -*-


from Conversion import century


def err (argument):

    return "Function Century - Argument \033[34m{0}\033[37m".format (argument)


assert century (1905) == 20, err (1905)

assert century ('1905') == 20, err ('1905')

assert century (1700) == 17, err (1700)

assert century (200) == 2, err (200)

assert century (-200) == 2, err (-200)

