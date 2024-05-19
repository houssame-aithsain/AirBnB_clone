#!/usr/bin/python3
""" about the console module """

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models import storage
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
import cmd
import re


cClass = {'User': User, 'BaseModel': BaseModel,
          'Amenity': Amenity, 'City': City, 'State': State,
          'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for the AirBnB project."""

    prompt = "(hbnb) "

    def do_update(self, arg: str):
        """Updates an instance based on the class name and id."""
        args = arg.split(maxsplit=3)
        if not validate_classname(args, check_id=True):
            return

        objsINC = storage.all()
        key = "{}.{}".format(args[0], args[1])
        repINC = objsINC.get(key, None)
        if repINC is None:
            print("** no instance found **")
            return

        mJSON = re.findall(r"{.*}", arg)
        if not validate_attrs(args):
            return
        if mJSON:
            payLOAD = None
            try:
                payLOAD: dict = json.loads(mJSON[0])
            except Exception:
                print("** invalid syntax")
                return
            for i, j in payLOAD.items():
                setattr(repINC, i, j)
            storage.save()
            return
        fattr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if fattr:
            setattr(repINC, args[2], fattr[0])
        else:
            vlist = args[3].split()
            setattr(repINC, args[2], parse_str(vlist[0]))
        storage.save()

    def precmd(self, command_line):
        """Defines instructions to execute before <line> is interpreted.
        """
        if not command_line:
            return '\n'

        pt = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        mline = pt.findall(command_line)
        if not mline:
            return super().precmd(command_line)

        mt = mline[0]
        if not mt[2]:
            if mt[1] == "count":
                objsINCE = storage.all()
                print(len([
                    v for _, v in objsINCE.items()
                    if type(v).__name__ == mt[0]]))
                return "\n"
            return "{} {}".format(mt[1], mt[0])
        else:
            args = mt[2].split(", ")
            if len(args) == 1:
                return "{} {} {}".format(
                    mt[1], mt[0],
                    re.sub("[\"\']", "", mt[2]))
            else:
                match_json = re.findall(r"{.*}", mt[2])
                if (match_json):
                    return "{} {} {} {}".format(
                        mt[1], mt[0],
                        re.sub("[\"\']", "", args[0]),
                        re.sub("\'", "\"", match_json[0]))
                return "{} {} {} {} {}".format(
                    mt[1], mt[0],
                    re.sub("[\"\']", "", args[0]),
                    re.sub("[\"\']", "", args[1]), args[2])

    def do_create(self, arg):
        """Creates a new instance."""
        args = arg.split()
        if not validate_classname(args):
            return

        nobj = cClass[args[0]]()
        nobj.save()
        print(nobj.id)

    def do_EOF(self, line):
        """Inbuilt EOF command to gracefully catch errors."""
        print("")
        return True

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        objsINCE = storage.all()
        key = "{}.{}".format(args[0], args[1])
        rqINCE = objsINCE.get(key, None)
        if rqINCE is None:
            print("** no instance found **")
            return
        print(rqINCE)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        rqINCE = objs.get(key, None)
        if rqINCE is None:
            print("** no instance found **")
            return

        del objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances."""
        args = arg.split()
        objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in objs.items()])
            return
        if args[0] not in cClass.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v))
                  for _, v in objs.items() if type(v).__name__ == args[0]])
            return

    def do_help(self, arg):
        """To get help on a command, type help <topic>."""
        return super().do_help(arg)

    def emptyline(self):
        """ Called when an empty line is entered in response to the prompt."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True


def validate_attrs(args):
    """checks if attribute name and value are present"""
    if len(args) < 4:
        print("** value missing **")
        return False
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    return True


def validate_classname(args, check_id=False):
    """validates class name and id"""
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in cClass.keys():
        print("** class doesn't exist **")
        return False
    return True


def is_float(numbr):
    """Checks if `numbr` is float.
    """
    try:
        a = float(numbr)
    except (TypeError, ValueError):
        return False
    else:
        return True


def parse_str(arg):
    """Parses `arg` to an `int`, `float` or `string` if possible."""
    parcer = re.sub("\"", "", arg)

    if is_int(parcer):
        return int(parcer)
    elif is_float(parcer):
        return float(parcer)
    else:
        return arg


def is_int(x):
    """if `x` is int."""
    try:
        j = float(x)
        h = int(j)
    except (TypeError, ValueError):
        return False
    else:
        return j == h


if __name__ == "__main__":
    HBNBCommand().cmdloop()
