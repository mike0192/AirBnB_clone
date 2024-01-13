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

    def do_create(self, args):
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
    def do_show(self, args):
    """
    Command that prints the string representation of an instance
    based on class name and id

    Usage: show <class_name> <id>
    """
    try:
        if not args:
            raise SyntaxError()

        split_args = args.split(" ")

        if split_args[0] not in self.model_classes:
            raise NameError()

        if len(split_args) < 2:
            raise IndexError()

        model_obj = storage.all()
        key = split_args[0] + '.' + split_args[1]

        if key in model_obj:
            print(model_obj[key])
        else:
            raise KeyError()
    except SyntaxError:
        print("** class name missing **")
    except NameError:
        print("** class doesn't exist **")
    except IndexError:
        print("** instance id missing **")
    except KeyError:
        print("** no instance found **")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
