
PROMPT = " > "


class FieldError(Exception):
    def __init__(self, message: str="Field Error", status="Internal", *args, **kwargs):
        self.status = status
        self.message = message
        super().__init__({'status': self.status, 'message': self.message})

class FormError(FieldError):
    def __init__(self, message: str="Form Error", status="Internal", *args, **kwargs):
        super().__init__(message, status, *args, **kwargs)


class Field:
    def __init__(self, name=None, text=None, typing=None, validator=None, error_message=None,required=False, prompt=None):
        if name is None:
            raise FieldError("Field name is required")
        self.name = name
        self.text = text or name
        self.typing = typing
        self.validator = validator
        self.error_message = error_message
        self.required = required
        self.prompt = prompt

    def ask(self, question=None, error_message=None, prompt=None):
        prompt = prompt or self.prompt
        question = question or self.text
        error_message = self.error_message or error_message
        value = input(f"{question}{"*" if self.required else ""}{prompt}")
        if self.required:
            if not value:
                print(error_message)
                return self.ask(question, error_message, prompt)
        else:
            if not value:
                return None
        if self.typing is not None:
            try:
                if self.typing == bool:
                    value = bool(int(value))
                else:
                    value = self.typing(value)
            except Exception:
                print(error_message or "")
                return self.ask(question, error_message, prompt)
        if self.validator:
            if not self.validator(value):
                print(error_message or "")
                return self.ask(question, error_message, prompt)
        return value

class ListField:
    def __init__(self, name=None, text=None, choices=None, prompt=None, error_message=None, required=False):
        exception_message = "ListField is list or tuple of two elements value and display, or a str as value"
        self.choices = {}
        if name is None:
            raise FieldError("Field name is required")
        self.name = name
        self.text = text or name
        self.prompt = prompt
        self.error_message = error_message
        self.required = required
        index = 1
        for choice in choices:
            if isinstance(choice, (list, tuple)):
                if len(choice) != 2:
                    raise FieldError(exception_message)
                self.choices[index] = {"value": choice[0], "display": choice[1]}
            elif isinstance(choice, str):
                self.choices[index] = {"value": choice, "display": choice}
            else:
                raise FieldError(exception_message)
            index += 1

    def ask(self, question=None, error_message=None, prompt=None):
        prompt = self.prompt or prompt
        error_message = self.error_message or error_message
        # question = question or self.text
        print(f"{self.text}{'*' if self.required else ''}")
        for choice in self.choices:
            print(f"{choice:<5}- {self.choices[choice]["display"]}")
        response = Field(
            name="response", text=" ", typing=int, required=self.required, validator=lambda x: x in self.choices,
            prompt=prompt, error_message=error_message).ask()
        return self.choices[response]["value"] if response else None

class Form:
    def __init__(self, fields: list = None, validator=None, error_message=None, prompt=PROMPT):
        self.fields = fields
        self.validator = validator
        self.error_message = error_message
        self.prompt = prompt

    def add_fields(self, fields):
        for field in fields:
            self.add_field(field)

    def add_field(self, field):
        self.fields.append(field)

    def ask(self):
        self.data = {}
        for field in self.fields:
            if field.name in self.data:
                raise FormError(f"Field {field.name} already exists")
            if not isinstance(field, (Field, ListField)):
                raise FormError("Field must be a Field or ListField")
            if isinstance(field, Field):
                question = field.text or field.name
                self.data[field.name] = field.ask(question, self.error_message, self.prompt)
                # self.data[field.name] = field.value
            elif isinstance(field, ListField):
                # for choice in field.choices:
                self.data[field.name] = field.ask(field.name, self.error_message, self.prompt)
        return self.data


def ask_confirm(message="Are you sure ?", callback_no=None, callback_yes=None, prompt=PROMPT, default="y"):
    """Ask yes or no, only the callback_no is required"""
    if callback_no is None or not callable(callback_no):
        raise FieldError("callback_no function is missing or is not callable", "Internal")
    if callback_yes is not None and not callable(callback_yes):
        raise FieldError("callback_yes expects a callable or None", "Internal")
    choices = {"y": callback_yes, "n": callback_no}
    display_choices = []
    if not default:
        if default not in ["y", "Y", "n", "N", None]:
            raise FormError("Invalid default value, must be None, 'y' or 'n'", "Internal")
    else:
        default = default.lower().strip()
    for choice in choices:
        choice = choice.upper() if choice == default else choice.lower()
        display_choices.append(choice)
    confirmation = input(f"{message} ({display_choices[0]}/{display_choices[1]}){prompt}").lower().strip()
    if not confirmation and confirmation is not None:
        confirmation = default
    if confirmation not in choices:
        return ask_confirm(message, callback_no, callback_yes, prompt, default)
    if choices[confirmation] is not None:
        choices[confirmation]()


class Menu:
    # TODO: Implement a menu class
    pass