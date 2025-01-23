#! /usr/bin/env python3

"""
color parameters: style;background (30 is none);foreground
example:
c = Color
print(f"{c.info}This is an info message{c.end}")
"""

from .ascii_map_01 import abc_map_01 as abc_map

print(abc_map)

class Color:
    end = "\x1b[0m"
    cyan    =    info       = "\x1b[0;30;36m"
    green   =    success    = "\x1b[0;30;32m"
    yellow  =    warning    = "\x1b[0;30;33m"
    red     =    danger     = "\x1b[0;30;31m"
    blue = "\x1b[0;30;34m"
    grey = "\x1b[0;30;30m"
    violet = "\x1b[0;30;30m"

    bg_black = "\x1b[5;30;40m"
    bg_grey = "\x1b[5;37;30m"
    bg_red = "\x1b[5;30;41m"
    bg_green = "\x1b[5;30;42m"
    bg_yellow = "\x1b[5;30;43m"
    bg_blue = "\x1b[5;30;44m"
    bg_cyan = "\x1b[5;30;46m"
    bg_violet = "\x1b[5;30;45m"
    bg_white = "\x1b[5;30;47m"


class TitleArt:
    def __init__(self, text="", abc_map=abc_map, color=None, jump=0):
        self.height = len(abc_map["a"])
        self.text = text.lower()
        self.color = color is not None
        self.display = color or ""
        self.jump = jump

        self.build_display()

    def build_display(self):
        for row in range(self.height):
            display = ""
            for i in range(len(self.text)):
                letter = self.text[i]
                display += abc_map[letter][row][self.jump:]
            self.display += display + "\n"
        if self.color:
            self.display += Color.end

    def jumper(display, letter_line, jump):
        temp_display = display
        for i in range(jump):
            if display[-jump] == " ":
                display[-jump] = letter_line[0]

    def __str__(self):
        return self.display
