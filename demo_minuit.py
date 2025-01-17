#! /usr/bin/env python3

from pprint import pprint

from silly_engine import Field, Form, ListField, ask_confirm
from silly_engine import c, Logger

logger = Logger("Minuit")
logger.info("Let the demo begin here with a RPG character creation")

character_form = Form([
        Field("name", required = True, error_message=f"{c.warning}A name is required{c.end}"),
        # Field("Strength", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Strength must be a positive number{c.end}", required=True),
        # Field("Mana", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Mana must be a positive number{c.end}"),
        # ListField(
        #     "occupation", "\nYour ocupation ?", choices=[( "bar", "Barbarian"), ("mag", "Magician"), ("thi", "Thieve"), ("other", "Other")],
        #     error_message=f"{c.warning}Enter a number from 1 to 4{c.end}"
        #     ),
        # Field("working", text="currently working ?", typing=bool, error_message=f"{c.warning}Invalid value entered, choose 0 or 1{c.end}", required=True),
    ])


def form_view():
    data = character_form.ask()
    ask_confirm("Is it exact ?", callback_no=character_form.ask)
    print("you just entered:")
    pprint(data)


if __name__ == "__main__":
    form_view()
