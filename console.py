#!/usr/bin/python3
""" This script defines a class HBNBCommand """
import cmd


class HBNBCommand(cmd.Cmd):
    """ This class contains the entry point of the command interpreter. """
    prompt = '(hbnb) '

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
