#! /usr/bin/env python3
# coding: utf-8


from datetime import datetime


def str_to_date(string):
    date = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    return date

