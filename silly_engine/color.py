#! /usr/bin/env python3

"""
color parameters: style;background (30 is none);foreground
example:
c = Color
print(f"{c.info}This is an info message{c.end}")
"""


class Color:
    end = "\x1b[0m"
    info = "\x1b[0;30;36m"
    success = "\x1b[0;30;32m"
    warning = "\x1b[0;30;33m"
    danger = "\x1b[0;30;31m"

