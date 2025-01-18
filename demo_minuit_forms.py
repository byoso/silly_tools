#! /usr/bin/env python3

from pprint import pprint

from silly_engine import Field, Form, ListField, ConfirmField
from silly_engine import c, Logger

logger = Logger("Minuit")
logger.info("Let the demo begin here with a RPG character creation")

character_form = Form([
        Field("name", required = True, error_message=f"{c.warning}A name is required{c.end}"),
        Field("Strength", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Strength must be a positive number{c.end}", required=True),
        Field("Mana", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Mana must be a positive number{c.end}"),
        ListField(
            "occupation", "\nYour ocupation ?", choices=[( "bar", "Barbarian"), ("mag", "Magician"), ("thi", "Thieve"), ("other", "Other")],
            required=True, error_message=f"{c.warning}Enter a number from 1 to 4{c.end}"
            ),
        Field("flying", text="can fly ?", typing=bool, error_message=f"{c.warning}Invalid value entered, choose 0 or 1{c.end}", required=True),
        ConfirmField(message="Confirmed ?", default=True, recap=True),
    ])


def form_view():
    data = character_form.ask()
    print("\nyou just entered:")
    pprint(data)


if __name__ == "__main__":
    form_view()
