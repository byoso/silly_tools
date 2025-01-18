#! /usr/bin/env python3

from silly_engine import Field, Form, ListField, ConfirmField, Menu
from silly_engine import c, Logger

logger = Logger("Minuit")
logger.info("Let the demo begin here with a RPG character creation")

characters = [
    {"name": "Conan", "occupation": "Barbarian", "Strength": 10, "Mana": 0, "flying": False},
    {"name": "Merlin", "occupation": "Magician", "Strength": 0, "Mana": 10, "flying": True},
    {"name": "Robin", "occupation": "Thieve", "Strength": 5, "Mana": 5, "flying": False},
    {"name": "Gandalf", "occupation": "Magician", "Strength": 0, "Mana": 10, "flying": True},
]


character_form = Form([
        Field("name", required = True, error_message=f"{c.warning}A name is required{c.end}"),
        Field("Strength", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Strength must be a positive number{c.end}", required=True),
        Field("Mana", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Mana must be a positive number{c.end}"),
        ListField(
            "occupation", "\nYour ocupation ?", choices=("Barbarian", "Magician", "Thieve", "Other"),
            error_message=f"{c.warning}Enter a number from 1 to 4{c.end}"
            ),
        Field("flying", text="can fly ?", typing=bool, error_message=f"{c.warning}Invalid value entered, choose 0 or 1{c.end}", required=True),
        ConfirmField(message="Confirmed ?", default=True, recap=True),
    ])

def create_view():
    data = character_form.ask()
    characters.append(data)
    print("\nyou just entered:")
    print(data)
    menu.ask()

def exit_view():
    print("Goodbye !!")
    quit()

def list_view():
    print(f"{'---- Characters ----':=^80}")
    print("-" * 60)
    if len(characters) == 0:
        print("---- No characters yet ----")
        menu.ask()
    index = len(characters)
    print(f"{'index':<10}{'name':<20}{'Strength':<15}{'Mana':<10}{'occupation':<20}{'can fly':<15}")
    for i in range(index):
        print(f"{i:<10}{characters[i]['name']:<20}{characters[i]['Strength']:<15}{characters[i]['Mana']:<10}{characters[i]['occupation']:20}{characters[i]['flying']:<15}")
    menu.ask()

def edit_view():
    index = Field("index", text="Which character do you want to edit ?", typing=int).ask()
    if index is None:
        menu.ask()
    data = character_form.ask()
    characters[index] = data
    print("\nyou just entered:")
    print(data)
    menu.ask()

menu = Menu([
    (1, "create a character", create_view),
    (2, "list characters", list_view),
    (3, "edit character", edit_view),
    ("d", "create a character", exit_view),
    ("e", "create a character", exit_view),
    ("x", "exit", exit_view)],
            title="RPG Now !!", )


if __name__ == "__main__":
    menu.ask()