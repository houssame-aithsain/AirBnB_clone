#!/usr/bin/python3
"""This module defines the entry point of the command interpreter."""

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


cClass = {'BaseModel': BaseModel, 'User': User,
                   'Amenity': Amenity, 'City': City, 'State': State,
                   'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """The command interpreter"""

    prompt = "(hbnb) "

    def precmd(self, line):
        """Defines instructions to execute before <line> is interpreted.
        """
        if not line:
            return '\n'

        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        mline = pattern.findall(line)
        if not mline:
            return super().precmd(line)

        mt = mline[0]
        if not mt[2]:
            if mt[1] == "count":
                objs_inc = storage.all()
                print(len([
                    v for _, v in objs_inc.items()
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


    def do_EOF(self, line):
        """Inbuilt EOF command to gracefully catch errors.
        """
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance.
        """
        args = arg.split()
        if not validate_classname(args):
            return

        new_obj = cClass[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        """
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        objs_inc = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = objs_inc.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return
        print(req_instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
        """
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        objs_inc = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = objs_inc.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        del objs_inc[key]
        storage.save()

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
        if mJSON:
            payLOAD = None
            try:
                payLOAD: dict = json.loads(mJSON[0])
            except Exception:
                print("** invalid syntax")
                return
            for k, v in payLOAD.items():
                setattr(repINC, k, v)
            storage.save()
            return
        if not validate_attrs(args):
            return
        fattr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if fattr:
            setattr(repINC, args[2], fattr[0])
        else:
            value_list = args[3].split()
            setattr(repINC, args[2], parse_str(value_list[0]))
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
        """Override default `empty line + return` behaviour."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

def validate_classname(args, check_id=False):
    """Runs checks on args to validate classname entry.
    """
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in cClass.keys():
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True


def validate_attrs(args):
    """Runs checks on args to validate classname attributes and values.
    """
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True


def is_float(x):
    """Checks if `x` is float.
    """
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def is_int(x):
    """Checks if `x` is int.
    """
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def parse_str(arg):
    """Parse `arg` to an `int`, `float` or `string`.
    """
    parsed = re.sub("\"", "", arg)

    if is_int(parsed):
        return int(parsed)
    elif is_float(parsed):
        return float(parsed)
    else:
        return arg


if __name__ == "__main__":
    HBNBCommand().cmdloop()
