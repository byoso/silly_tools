"""
This script allows to create veeeery quicly a CLI

Example:

if __name__ == "__main__":
    cli.route(
        ("", main),
        ("-h", cli.help),
        ("--help", cli.help),
        ("see <int:a> <bool:> <str:> <float:>", see),
        ("test 2", test2),
        ("calc <float:a> <float:b>", calc)
    )

Each route takes a path with or without parameters '<>', and a callback
function that revieve the parameters if there are some.

that's all !
note that cli.help is an auto-created help.
"""


import sys


class CLI_Error(Exception):
    pass


def find_route(commands, routes, index=0):
    """Helper used within CLI, recursive."""
    if len(commands) < index:
        raise CLI_Error("CLI route not found")
    if len(commands) == 0:
        routes = [route for route in routes if route['path'] == '']
        if len(routes) != 1:
            raise CLI_Error("Bad routing")
    if len(routes) == 1:
        return routes[0]

    best = []
    for route in routes:
        if len(route['actions']) > index and len(commands) > index:
            if route['actions'][index] == commands[index]:
                best.append(route)
    index += 1

    return find_route(commands, best, index)


class CLI:
    def __call__(self):
        print(sys.argv)

    def route(self, *args):
        """
        CLI.route takes the place of an __init__ method, but is explicit.
        args are tuples like this:
        ("path", function)
        """
        self.routes = []

        for arg in args:
            self.set_route(arg)

        command = sys.argv
        self.decode_command(command)

    def set_route(self, arg):
        path = arg[0]
        function = arg[1]
        elems = path.strip().split(" ")
        actions = []
        arguments = []
        now_parameters = False
        for elem in elems:
            if elem.startswith("<"):
                now_parameters = True
                if elem.startswith("<int:"):
                    arguments.append(int)
                elif elem.startswith("<float:"):
                    arguments.append(float)
                elif elem.startswith("<bool:"):
                    arguments.append(bool)
                else:
                    arguments.append(str)
            else:
                if now_parameters:
                    raise CLI_Error("actions must not be set after parameters")
                actions.append(elem)

        self.routes.append({
            'path': path.strip(),
            'actions': actions,
            'function': function,
            'arguments': arguments
            })

    def decode_command(self, command):
        commands = command[1:]
        routes = self.routes[:]

        route = find_route(commands, routes)

        index = len(route['actions'])
        args = commands[index:]
        if len(args) <= len(route['arguments']):
            min = len(args)
            max = None
        else:
            min = len(route['arguments'])
            max = len(args)

        params = []
        for i in range(min):
            params.append(route['arguments'][i](args[i]))

        if max is not None:
            params = [*params, *args[min:max]]

        # print(route)
        return route['function'](*params)

    def help(self):
        message = "| ===         CLI options:                ===\n"
        for route in self.routes:
            if route['path'] == '':
                message += '| == Is also executable without any option == \n'
            else:
                descr = route['function'].__name__
                message += "| " + route['path'] + " -> " + f"{descr}" + "\n"
        print(message)


cli = CLI()
