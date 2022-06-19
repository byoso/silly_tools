#! /usr/bin/env python3
# coding: utf-8

import os


def check_pip():
    """Checks if pip is installed, if it is not,
    closes the program with a message"""
    res = os.popen("python3 -m pip -V").read().strip()
    OK = False
    if res.startswith('pip'):
        OK = True
    # if OK:  # debug
    if not OK:
        this_file = os.path.basename(__file__)
        print(
            "\x1b[0;30;33m"
            "pip is not installed for your main version of python3.\n"
            "\x1b[0m"
            "Please install pip first (see below)"
            ", and then, restart your session "
            f"before executing './{this_file}' again.\n\n"
            "   INSTALLING pip:\n"
            "- DEBIAN (Ubuntu, Linux Mint, etc...):\n"
            "sudo apt install python3-pip\n"
            "- Fedora, CentOS/RHEL 7+:\n"
            "sudo yum install python3-pip\n"
            "- ARCH LINUX, Manjaro:\n"
            "sudo pacman -S python-pip\n"
            "- OPENSUSE:\n"
            "sudo zypper install python3-pip\n"
            "\n"
            "Or, for any distribution:\n"
            "wget https://bootstrap.pypa.io/get-pip.py\n"
            "chmod +x get-pip.py\n"
            "sudo python3 get-pip.py\n"
            )
        exit()


check_pip()  # insert where you whant to check pip


# print("program doing things")
