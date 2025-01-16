#! /usr/bin/env python3

from silly_engine import Field, Form, ListField
from silly_engine import c, Logger

logger = Logger("Minuit")
logger.info("This is a demo of the minuit module")

form = Form([
        Field("name", required = True, error_message=f"{c.warning}A name is required{c.end}"),
        Field("age", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Age must be a positive number{c.end}"),
        ListField(
            "occupation", "\nYour ocupation ?", choices=[( "dev", "Developer"), ("des", "Designer"), ("man", "Manager"), ("other", "Other")],
            error_message=f"{c.warning}Enter a number from 1 to 4{c.end}",
            # required=True
            ),
        Field("working", text="currently working ?", typing=bool, error_message=f"{c.warning}Invalid value entered, choose 0 or 1{c.end}", required=True),
    ])

data = form.ask()

print(data)
