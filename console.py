#!/usr/bin/python3
"""
Console module to create a command interpreter for the AirBnB clone
"""
import cmd
import shlex  # For splitting the command line into arguments
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
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        new_instance = eval(f"{class_name}()")
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        args = shlex.split(arg)
        all_objs = storage.all()
        if len(args) == 0:
            print([str(all_objs[obj]) for obj in all_objs])
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        print([str(all_objs[obj]) for obj in all_objs if obj.startswith(class_name)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in ["BaseModel", "User"]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        obj = all_objs[key]
        if hasattr(obj, attribute_name):
            attr_type = type(getattr(obj, attribute_name))
            try:
                if attr_type is str:
                    setattr(obj, attribute_name, str(attribute_value))
                elif attr_type is int:
                    setattr(obj, attribute_name, int(attribute_value))
                elif attr_type is float:
                    setattr(obj, attribute_name, float(attribute_value))
                else:
                    print("** unsupported attribute type **")
                    return
            except ValueError:
                print("** invalid value type **")
                return
        else:
            print("** attribute doesn't exist **")
            return

        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
