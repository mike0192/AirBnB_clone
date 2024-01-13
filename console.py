#!/usr/bin/python3

"""Console for the command line
   interpretation
"""
import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file),
        and prints the id

        Usage: create <class_name>
        """

        try:
            if not args:
                raise SyntaxError()

            split = args.split(" ")
            instance = eval("{}()".format(split[0]))

            for cmd_arg in split[1:]:
                parameter = cmd_arg.split("=")
                key = parameter[0]
                value = parameter[1].replace("_", " ")

                if hasattr(instance, key):
                    try:
                        setattr(instance, key, eval(value))
                    except Exception:
                        pass

            instance.save()

            print("{}".format(instance.id))
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            pass

    def do_quit(self, arg):
        """Quit the program"""
        "Exit"
        return True

    def emptyline(self):
        """Emptyline should be passed and don't do
           anything
        """
        pass

    def do_EOF(self, arg):
        """Exit the program"""
        "Exit"
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
