#! /usr/bin/env python3

"""
color parameters: style;background (30 is none);foreground
example:
c = Color
print(f"{c.info}This is an info message{c.end}")
"""


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
