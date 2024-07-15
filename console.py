#!/usr/bin/python3
"""Console command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def do_create(self, arg):
        """Create a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        cls = globals()[class_name]
        obj = cls()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Show an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, obj_id = args[0], args[1]
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Destroy an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name, obj_id = args[0], args[1]
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Show all instances or all instances of a class"""
        if arg and arg not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        objs = storage.all()
        if not arg:
            print([str(v) for v in objs.values()])
            return

        class_name = arg
        filtered_objs = [str(v) for k, v in objs.items() if k.startswith(class_name)]
        print(filtered_objs)

    def do_update(self, arg):
        """Update an instance based on class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if len(args) < 3:
            print("** instance id missing **")
            return

        class_name, obj_id, attr_name = args[0], args[1], args[2]
        if class_name not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        value = " ".join(args[3:])
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        obj = storage.all()[key]
        if attr_name not in obj.__class__.__dict__:
            print("** attribute name missing **")
            return

        # Cast value to appropriate type
        attr_type = type(obj.__class__.__dict__[attr_name])
        if attr_type == str:
            setattr(obj, attr_name, value)
        elif attr_type == int:
            setattr(obj, attr_name, int(value))
        elif attr_type == float:
            setattr(obj, attr_name, float(value))
        
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
