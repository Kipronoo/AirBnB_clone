#!/usr/bin/python3
"""
Console module to create a command interpreter for the AirBnB clone
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone"""

    prompt = '(hbnb) '
    
    def __init__(self):
        """Initialize the command interpreter"""
        super().__init__()

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of File command to exit the program"""
        print()  # For new line after EOF
        return True

    def do_help(self, arg):
        """Help command to show help for commands"""
        super().do_help(arg)

    def emptyline(self):
        """Override empty line behavior"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
