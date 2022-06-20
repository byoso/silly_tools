"""Installs some dependencies within the script
NOT PEP8 friendly !
"""


import os
import sys
import pkg_resources

version = sys.version_info  # python version used
this_file = os.path.basename(__file__)

dependencies = [
    'flamewok>=1.0.7',
]
try:
    pkg_resources.require(dependencies)
except pkg_resources.DistributionNotFound:
    os.system(
        f"python{version[0]}.{version[1]} "
        "-m pip install --upgrade flamewok")
    if f"{version[0]}.{version[1]}" not in ["3.6", "3.9"]:
        print(
            "\x1b[0;30;32m"
            f"Dependencies installed, please, execute '{this_file}' again"
            "\x1b[0m"
            )
        exit()
