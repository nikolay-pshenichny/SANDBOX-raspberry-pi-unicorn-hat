#!/usr/bin/env python

import unicornhat as hat
import time, math


hat.brightness(0.1)


for x in range(8):
    hat.set_pixel(x, 1, x * 20, 0, 0)
    hat.set_pixel(x, 2, 0, x * 20, 0)
    hat.set_pixel(x, 3, 0, 0, x * 20)
    hat.set_pixel(x, 4, x * 20, x * 20, 0)
    hat.set_pixel(x, 5, 0, x * 20, x * 20)
    hat.set_pixel(x, 6, x * 20, x * 20, x * 20)
hat.show()
input("press enter to stop")

