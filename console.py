#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNH console """
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exits console"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Print empy line"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
