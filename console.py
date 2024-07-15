#!/usr/bin/python3
"""
Console module to create a command interpreter for the AirBnB clone
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB clone"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """End of File command to exit the program"""
        print()  # Print newline for clean exit
        return True

    def do_help(self, arg):
        """Help command to show help for commands"""
        super().do_help(arg)

    def emptyline(self):
        """Override empty line behavior"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a class, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        if arg not in storage.classes:
            print("** class doesn't exist **")
            return

        cls = storage.classes[arg]
        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{args[0]}.{instance_id}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{args[0]}.{instance_id}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = arg.split()
        if len(args) > 1:
            print("** class name missing **")
            return

        if len(args) == 1 and args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        objs = []
        if len(args) == 0:
            objs = storage.all().values()
        else:
            objs = [obj for key, obj in storage.all().items() if key.startswith(args[0])]

        print([str(obj) for obj in objs])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in storage.classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{args[0]}.{instance_id}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) == 3:
            print("** value missing **")
            return

        attribute_value = args[3].strip('"')
        if hasattr(obj, attribute_name):
            attr_type = type(getattr(obj, attribute_name))
            if attr_type is str:
                setattr(obj, attribute_name, attribute_value)
            elif attr_type is int:
                setattr(obj, attribute_name, int(attribute_value))
            elif attr_type is float:
                setattr(obj, attribute_name, float(attribute_value))
            else:
                print("** unsupported attribute type **")
                return
        else:
            print("** attribute name missing **")
            return

        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
