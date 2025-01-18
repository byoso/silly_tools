
PROMPT = " > "

def confirmation_displayer(data):
    print("\n== Check before confirmation ==" + "="*49)
    for key in data:
        print(f"- {key:<20}: {data[key]}")
    print("="*80)


class FieldError(Exception):
    def __init__(self, message: str="Field Error", status="Internal", *args, **kwargs):
        self.status = status
        self.message = message
        super().__init__({'status': self.status, 'message': self.message})


class FormError(FieldError):
    def __init__(self, message: str="Form Error", status="Internal", *args, **kwargs):
        super().__init__(message, status, *args, **kwargs)


class ConfirmField:
    def __init__(self, message="Are you sure ?", yes="y", no="n", default=True, prompt=PROMPT, displayer=confirmation_displayer, recap=False):
        self.message = message
        self.yes_no_message = f"({yes}/{no})"
        self.yes = yes
        self.no = no
        self.displayer = displayer
        self.recap = recap
        self.default = default
        self.prompt = prompt
        self.validator = lambda x: x.strip().lower() in [yes, no, ""]
        if default not in [True, False, None]:
            raise FieldError(f"default must be a boolean value or None, received '{default}'", "Internal")
        if default == True:
            self.yes_no_message = f"({yes.upper()}/{no})"
        if default == False:
            self.yes_no_message = f"({yes}/{no.upper()})"


    def ask(self):
        value = input(f"{self.message}{self.yes_no_message}{self.prompt}")
        if self.validator:
            if not self.validator(value):
                return self.ask()
        resolve = {self.yes: True, self.no: False}
        if value.strip() == "":
            if self.default is None:
                return self.ask()
            return self.default
        else:
            return resolve[value.strip().lower()]



class Field:
    def __init__(self, name=None, text=None, typing=None, validator=None, error_message=None,required=False, prompt=None, default=None, is_confirmator=False):
        if name is None:
            raise FieldError("Field name is required")
        self.name = name
        self.text = text or name
        self.typing = typing
        self.validator = validator
        self.error_message = error_message
        self.required = required
        self.prompt = prompt
        self.default = default
        self.is_confirmator = is_confirmator

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
                return self.default
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
        confirmed = False
        while confirmed is False:
            confirmed = True
            self.data = {}
            for field in self.fields:
                if not isinstance(field, ConfirmField) and field.name in self.data:
                    raise FormError(f"Field {field.name} already exists")
                if not isinstance(field, (Field, ListField, ConfirmField)):
                    raise FormError("Field must be a Field, ListField or ConfirmField")
                if isinstance(field, Field):
                    question = field.text or field.name
                    self.data[field.name] = field.ask(question, self.error_message, self.prompt)
                elif isinstance(field, ListField):
                    self.data[field.name] = field.ask(field.name, self.error_message, self.prompt)
                elif isinstance(field, ConfirmField):
                    if field.recap and callable(field.displayer):
                        field.displayer(self.data)
                    response = field.ask()
                    if response == False:
                        confirmed = False
        return self.data



class Menu:
    # TODO: Implement a menu class
    pass