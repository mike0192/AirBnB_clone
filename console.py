#!/usr/bin/python3

"""Console for the command line
   interpretation
"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit the program"""
        "Exit"
        return True

    def emptyline(self):
        """Emptyline should be passed and don't do
           anything
        """
        pass

    def do_EOF(self, args):
        """Exit the program"""
        "Exit"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
