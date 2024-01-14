#!/usr/bin/python3

"""Console for the command line
   interpretation
"""
import cmd
from models.base_model import BaseModel
from models import storage
from shlex import split
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    model_classes = {
            "BaseModel",
            "User",
            "Place",
            "Review",
            "State",
            "Amenity",
            "City"
            }

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

            split_args = args.split(" ")
            instance = eval("{}()".format(split_args[0]))

            for cmd_arg in split_args[1:]:
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

    def do_update(self, args):
        """
           Command that updates an instance based on the class name and id
           by adding or updating an attribute

           Usage: update <class name> <id> <attribute name> "<attribute value>"
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

    def do_destroy(self, args):
        """Command that deletes an instance of a class name and id
           and saves the change to the JSON file

           Usage: destroy <class name> <id>
        """
        try:
            if not args:
                raise SyntaxError()
            split_args = split(args, " ")
            split_args = args.split(" ")

            if split_args[0] not in self.model_classes:
                raise NameError()

            if len(split_args) < 2:
                raise IndexError()

            model_obj = storage.all()
            key = split_args[0] + '.' + split_args[1]

            if key not in model_obj:
                raise KeyError()

            if len(split_args) < 3:
                raise AttributeError()

            if len(split_args) < 4:
                raise ValueError()

            val = model_obj[key]

            try:
                val.__dict__[split_args[2]] = eval(split_args[3])
            except Exception:
                val.__dict__[split_args[2]] = split_args[3]
                val.save()

            if key in model_obj:
                del model_obj[key]
                storage.save()
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
        except AttributeError:
            print("** attribute name missing **")
        except ValueError:
            print("** value missing **")

    def do_all(self, args):
        """
        Command that prints all string representations of all instances
        based or not on the class name

        Usage: all <class name> or all
        """

        model_obj = storage.all()
        lists = []

        if not args:
            for key in model_obj:
                lists.append(model_obj[key])
            print(lists)
            return
        try:
            args = args.split(" ")
            if args[0] not in self.model_classes:
                raise NameError()
            for key in model_obj:
                name = key.split('.')
                if name[0] == args[0]:
                    lists.append(model_obj[key])
            print(lists)
        except NameError:
            print("** class doesn't exist **")

    def count(self, args):
        """Class that retrieves the number of instances of a class
           based on id
        """
        count_inst = 0
        try:
            lists = split(args, " ")
            if lists[0] not in self.model_classes:
                raise NameError()
            model_obj = storage.all()
            for key in model_obj:
                name = key.split('.')
                if name[0] == lists[0]:
                    count_inst += 1
            print(count_inst)
        except NameError:
            print("** class doesn't exist **")

    def divide_args(self, args):
        """Return the command string inside a class
           after stripping
        """

        new_list = []
        new_list.append(args[0])
        try:
            my_dict = eval(
                args[1][args[1].find('{'):args[1].find('}')+1])
        except Exception:
            my_dict = None
        if isinstance(my_dict, dict):
            new_string = args[1][args[1].find('(')+1:args[1].find(')')]
            new_list.append(((new_str.split(", "))[0]).strip('"'))
            new_list.append(my_dict)
            return new_list
        new_string = args[1][args[1].find('(')+1:args[1].find(')')]
        new_list.append(" ".join(new_str.split(", ")))
        return " ".join(i for i in new_list)

    def default(self, args):
        """Class that retrieves the number of
           instances
        """
        lists = args.split('.')
        if len(lists) >= 2:
            if lists[1] == "all()":
                self.do_all(lists[0])
            elif lists[1] == "count()":
                self.count(lists[0])
            elif lists[1][:4] == "show":
                self.do_show(self.devide_args(lists))
            elif lists[1][:7] == "destroy":
                self.do_destroy(self.devide_args(lists))
            elif lists[1][:6] == "update":
                line_args = self.devide_args(lists)
                if isinstance(line_args, list):
                    model_obj = storage.all()
                    k = args[0] + ' ' + args[1]
                    for key, value in args[2].items():
                        self.do_update(k + ' "{}" "{}"'.format(key, value))
                else:
                    self.do_update(line_args)
        else:
            cmd.Cmd.default(self, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
