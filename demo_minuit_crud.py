#! /usr/bin/env python3

from silly_engine import Field, Form, ListField, ConfirmField, Menu, clear, AutoArray
from silly_engine import c

WIDTH = 100  # try 100, 120

# a data set to begin with
characters = [
    {"name": "Conan", "occupation": "Barbarian", "strength": 90, "mana": None, "flying": False},
    {"name": "Merlin", "occupation": "Magician", "strength": 5, "mana": 10, "flying": True},
    {"name": "Robin", "occupation": "Thieve", "strength": 5, "mana": 5, "flying": False},
    {"name": "Gandalf", "occupation": "Magician", "strength": 10, "mana": 10, "flying": True},
]

character_form = Form([
        Field("name", required = True, error_message=f"{c.warning}A name is required{c.end}"),
        Field("strength", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Strength must be a positive number{c.end}", required=True, default=10),
        Field("mana", validator=lambda x: x>0, typing=int, error_message=f"{c.warning}Mana must be a positive number{c.end}"),
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
    characters.insert(0, data)
    clear()
    list_view()

def exit_view():
    clear()
    print("Goodbye !!")
    quit()

def list_view():
    clear()
    array = AutoArray(
        characters, title="Characters", width=WIDTH, color_1=c.bg_blue, color_2=c.bg_green,
        include=["name", "flying", "occupation", "mana", "strength"])
    print(array)
    menu.ask()

def edit_view():
    index = Field("index", text="Which character do you want to edit ?", typing=int, validator=lambda x: x < len(characters),
                  error_message=f"{c.warning}Invalid entry, enter a valid index{c.end}").ask()
    if index is None:
        list_view()
    character = characters[index]
    characters[index] = character_form.update(character)
    clear()
    list_view()

def delete_view():
    index = Field(
        "index", text="Which character do you want to delete ?", typing=int, validator=lambda x: x < len(characters),
        error_message=f"{c.warning}Invalid entry, enter a valid index{c.end}").ask()
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
            title="RPG Now !!",
            width=WIDTH, error_message=f"{c.warning}Invalid choice{c.end}",
            clear_on_error=True)


if __name__ == "__main__":
    clear()
    list_view()