
#!/usr/bin/env python3

# -*- coding: utf-8 -*-


def century (year):
    
    if year < 0:
        year = year * -1

    return (int(year) - 1 ) // 100 + 1