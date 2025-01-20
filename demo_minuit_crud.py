#! /usr/bin/env python3

from silly_engine import Field, Form, ListField, ConfirmField, Menu, clear
from silly_engine import c, Logger

WIDTH = 100

characters = [
    {"name": "Conan", "occupation": "Barbarian", "Strength": 90, "Mana": 0, "flying": False},
    {"name": "Merlin", "occupation": "Magician", "Strength": 5, "Mana": 10, "flying": True},
    {"name": "Robin", "occupation": "Thieve", "Strength": 5, "Mana": 5, "flying": False},
    {"name": "Gandalf", "occupation": "Magician", "Strength": 10, "Mana": 10, "flying": True},
]


character_form = Form([
        Field("name", required = True, error_message=f"{c.warning}A name is required{c.end}"),
        Field("Strength", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Strength must be a positive number{c.end}", required=True),
        Field("Mana", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Mana must be a positive number{c.end}"),
        ListField(
            "occupation", "\nYour ocupation ?", choices=("Barbarian", "Magician", "Thieve", "Other"),
            error_message=f"{c.warning}Enter a number from 1 to 4{c.end}"
            ),
        Field("flying", text="can fly ?", typing=bool, error_message=f"{c.warning}Invalid value entered, choose 0 or 1{c.end}", required=True)
    ])

def create_view():
    data = character_form.ask()
    confirmed = ConfirmField(message="Confirmed ?", default=True, recap=True).ask()
    if not confirmed:
        clear()
        list_view()
    characters.append(data)
    clear()
    print("\nyou just entered:")
    print(data)
    list_view()

def exit_view():
    clear()
    print("Goodbye !!")
    quit()

def list_view():
    clear()
    print(f"{'---- Characters ----':=^{WIDTH}}")
    if len(characters) == 0:
        print(f"\n{'---- No characters yet ----': ^{WIDTH}}")
        menu.ask()
    index = len(characters)
    print(f"{'index':<10}{'name':<20}{'Strength':<15}{'Mana':<10}{'occupation':<20}{'can fly':<15}")
    for i in range(index):
        print(
            f"{i:<10}{characters[i]['name']:<20}{characters[i]['Strength']:<15}{characters[i]['Mana'] or '---':<10}"
            f"{characters[i]['occupation'] or '---':20}{characters[i]['flying']:<15}")
    menu.ask()

def edit_view():
    index = Field("index", text="Which character do you want to edit ?", typing=int, validator=lambda x: x < len(characters),
                  error_message="Invalid entry, enter a valid index").ask()
    if index is None:
        list_view()
    character = characters[index]
    characters[index] = character_form.update(character)
    clear()
    list_view()

def delete_view():
    index = Field(
        "index", text="Which character do you want to delete ?", typing=int, validator=lambda x: x < len(characters),
        error_message="Invalid entry, enter a valid index").ask()
    if index is None:
        list_view()
    character = characters[index]
    confirm = ConfirmField(message=f"Are you sure you want to delete {character['name']} ?").ask()
    if confirm:
        characters.pop(index)
    clear()
    list_view()


menu = Menu([
    (1, "create a character", create_view),
    (2, "list characters", list_view),
    (3, "edit character", edit_view),
    (4, "delete a character", delete_view),
    ("x", "exit", exit_view)],
            title="RPG Now !!", width=WIDTH)


if __name__ == "__main__":
    clear()
    logger = Logger("Minuit")
    logger.info("Let the demo begin here with some RPG characters !")
    list_view()
    menu.ask()