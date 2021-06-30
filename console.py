#!/usr/bin/python3
""" This script defines a class HBNBCommand """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.engine.file_storage import FileStorage
import models


class HBNBCommand(cmd.Cmd):
    """ This class contains the entry point of the command interpreter. """
    prompt = '(hbnb) '
    list_classes = ['BaseModel', 'User', 'State', 'Review', 'Place',
                    'Amenity', 'City']

    def do_create(self, args):
        """ This method creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id. """
        words = args.split()
        if len(words) != 1:
            print("** class name missing **")
        elif words[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        else:
            dummy = eval(words[0])()
            dummy.save()
            print(dummy.id)

    def do_show(self, args):
        """ This method prints the string representation of an instance
            based on the class name and id. """
        words = args.split()
        list_ids = [v.id for v in models.storage.all().values()]
        if len(words) < 1:
            print("** class name missing **")
        elif len(words) == 1 and words[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 2 and words[1] not in list_ids:
            print('** no instance found **')
        else:
            instances = models.storage.all()
            id = words[0] + '.' + words[1]
            if id in instances:
                print(instances[id])
            else:
                print('** no instance found **')

    def do_destroy(self, args):
        """ This method deletes an instance based on the class name
            and id (save the change into the JSON file). """
        words = args.split()
        list_ids = [v.id for v in models.storage.all().values()]
        if len(words) < 1:
            print("** class name missing **")
        elif len(words) == 1 and words[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 2 and words[1] not in list_ids:
            print("** no instance found **")
        else:
            instances = models.storage.all()
            id = words[0] + '.' + words[1]
            if id in instances:
                FileStorage._FileStorage__objects.pop(id)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args=None):
        """ This method prints all string representation
            of all instances based or not on the class name. """
        if args and args not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif not args:
            print([str(value) for value in models.storage.all().values()])
        else:
            print([str(value) for value in models.storage.all().values()
                   if value.__class__.__name__ == args])

    def do_update(self, args):
        """ This method updates an instance based on the
            class name and id by adding or updating attribute
            (save the change into the JSON file). """
        words = args.split()
        list_ids = [v.id for v in models.storage.all().values()]
        if len(words) < 1:
            print("** class name missing **")
        elif len(words) == 1 and words[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(words) == 1:
            print("** instance id missing **")
        elif len(words) == 2 and words[1] not in list_ids:
            print("** no instance found **")
        elif len(words) == 2 and words[1] in list_ids:
            print("** attribute name missing **")
        elif len(words) == 3:
            print("** value missing **")
        else:
            main_dict = models.storage.all()
            id = words[0] + '.' + words[1]
            if id in main_dict:
                setattr(main_dict[id], words[2], words[3])
                models.storage.save()
            else:
                print("** no instance found **")

    def do_EOF(self, arg):
        """ This method exits of the console using Ctrl + D. """
        return True

    def do_quit(self, arg):
        """ This method exits of the program through quit command. """
        return True

    def emptyline(self):
        """ This method prints a new line when there is no command. """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
