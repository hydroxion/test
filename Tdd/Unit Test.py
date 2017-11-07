
#!/usr/bin/env python3

# -*- coding: utf-8 -*-


import unittest

import Conversion as cv


class TestConversion (unittest.TestCase):
    
    def test_century (self):

        self.assertEqual (cv.century (1905), 20)

        self.assertEqual (cv.century ('1905'), 20)

        self.assertEqual (cv.century (1700), 17)

        self.assertEqual (cv.century (200), 2)

        self.assertEqual (cv.century (-200), 2)


if __name__ == '__main__':

    unittest.main ()
