#!/usr/bin/env python

import unicornhat as hat
import time, math

BLACK_PIXEL = [0, 0, 0]
VIDEO_MEMORY_SIZE = 64

class GradientLine:
    _offset = None
    _gradient = []
    def __init__(self):
        self._offset = 0
        self._len = 3
        self._gradient = [[90, 90, 0], [160, 160, 0], [240, 240, 0]]

    def Show(self, video_memory):
        destination_addr = self._offset
        for source_addr in range(self._len):
            video_memory[destination_addr] = self._gradient[source_addr];
            destination_addr += 1;
            if (destination_addr >= VIDEO_MEMORY_SIZE):
                destination_addr = 0

    def Hide(self, video_memory):
        destination_addr = self._offset
        for source_addr in range(self._len):
            video_memory[destination_addr] = BLACK_PIXEL;
            destination_addr += 1;
            if (destination_addr >= VIDEO_MEMORY_SIZE):
                destination_addr = 0

    def Move(self):
         self._offset += 1
         if (self._offset >= VIDEO_MEMORY_SIZE):
             self._offset = 0

def AllocateVideoMemory(size = VIDEO_MEMORY_SIZE):
    # Creates a list with 64 black pixels
    result = []
    for x in range(size):
        result.append(BLACK_PIXEL)
    return result


def FlushVideoMemoryToUnicornHat(video_memory):
    video_memory_address = 0
    for y in range(8):
        for x in range(8):
            pixel_data = video_memory[video_memory_address]
            video_memory_address += 1
            red = pixel_data[0]
            green = pixel_data[1]
            blue = pixel_data[2]
            hat.set_pixel(x, y, red, green, blue)
    hat.show()



# Turn off the eye-burning mode
hat.brightness(0.05)

# Init an array that will serve as "video memory".
# ie. instead of two-dimensional 8x8 array, we are going to use one-dimentional array with 64 elements.
# in that array, first 8 items will represent first row, second 8 items - second row, etc.
video_memory = AllocateVideoMemory()

# Create a "gradient line" object. We will "project" it onto the video_memory and slowly move it
gradient_line = GradientLine()

while True:
    gradient_line.Show(video_memory)
    FlushVideoMemoryToUnicornHat(video_memory)
   
    time.sleep(0.05)

    gradient_line.Hide(video_memory)
    gradient_line.Move()