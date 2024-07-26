#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def do_create(self, args):
        if not args:
            print("** class name missing **")
            return
        if args not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[args]()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        class_name, instance_id = args_list
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = class_name + '.' + instance_id
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, args):
        args_list = args.split()
        if len(args_list) == 0:
            print("** class name missing **")
            return
        if len(args_list) == 1:
            print("** instance id missing **")
            return
        class_name, instance_id = args_list
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        if not args:
            obj_list = [str(obj) for obj in storage.all().values()]
        else:
            if args not in self.classes:
                print("** class doesn't exist **")
                return
            obj_list = [str(obj) for obj in storage.all().values() if isinstance(obj, self.classes[args])]
        print(obj_list)

    def do_update(self, args):
        args_list = args.split()
        if len(args_list) < 4:
            print("** value missing **")
            return
        class_name, instance_id, attr_name, attr_value = args_list[:4]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = class_name + '.' + instance_id
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            if hasattr(obj, attr_name):
                attr_type = type(getattr(obj, attr_name))
                setattr(obj, attr_name, attr_type(attr_value))
            else:
                setattr(obj, attr_name, attr_value)
            obj.save()

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        print("")
        return True

    def do_quit(self, arg):
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
