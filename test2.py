#!/usr/bin/env python

import unicornhat as hat
import time, math


hat.brightness(0.1)


while True:
    # R
    for c in range(255):
        for x in range(8):
            for y in range(8):
                hat.set_pixel(x, y, c, 0, 0)
        hat.show()
        #time.sleep(0.005)
    # G
    for c in range(255):
        for x in range(8):
            for y in range(8):
                hat.set_pixel(x, y, 0, c, 0)
        hat.show()
        #time.sleep(0.005)
    # B 
    for c in range(255):
        for x in range(8):
            for y in range(8):
                hat.set_pixel(x, y, 0, 0, c)
        hat.show()
        #time.sleep(0.005)