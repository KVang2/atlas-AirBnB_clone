#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
"""
Program that contains the entry point of command interpreter
"""



class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit program on EOF"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            print(storage.all().get(key, "** no instance found **"))
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_instances = storage.all()
            if key in all_instances:
                del all_instances[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_instances = storage.all()
        if not arg or args[0] not in storage.classes():
            print([str(obj) for obj in all_instances.values()])
        else:
            try:
                class_name = args[0]
                print([str(obj) for key, obj in all_instances.items()
                       if key.startswith(class_name)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            all_instances = storage.all()
            if key not in all_instances:
                print("** class doesn't exist **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attr_value = args[3]
            instance = all_instances[key]
            setattr(instance, attr_name, attr_value)
            instance.save()
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
