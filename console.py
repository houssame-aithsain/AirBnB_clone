#!/usr/bin/python3
"""This module defines the entry point of the command interpreter."""


import re
import cmd
import json
from models import storage
from models.base_model import BaseModel

current_classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project."""

    prompt = "(hbnb) "

    def precmd(self, line):
        """Preprocess the command line."""

        if not line:
            return '\n'
        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        match = pattern.match(line)
        if match:
            class_name = match.group(1)
            method_name = match.group(2)
            args = match.group(3)
            if method_name == "all":
                return "all {}".format(class_name)
            if method_name == "show":
                return "show {} {}".format(class_name, args)
            if method_name == "destroy":
                return "destroy {} {}".format(class_name, args)
            if method_name == "update":
                return "update {} {}".format(class_name, args)
            if method_name == "count":
                return "count {}".format(class_name)
        return line

    def do_quit(self, arg):
        """Quit command to exit the program.
        """
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program.
        """
        return True
    
    def emptyline(self):
        """Handles empty line.
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to JSON file and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in current_classes.keys():
            print("** class doesn't exist **")
            return
        new_instance = current_classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance.
        """
        args = arg.split()
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
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

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        del instance_objs[key]
        storage.save()

    def do_all(self, arg):
        """Prints string representation of all instances.
        """
        args = arg.split()
        all_objs = storage.all()

        if len(args) < 1:
            print(["{}".format(str(v)) for _, v in all_objs.items()])
            return
        if args[0] not in current_classes.keys():
            print("** class doesn't exist **")
            return
        else:
            print(["{}".format(str(v))
                  for _, v in all_objs.items() if type(v).__name__ == args[0]])
            return

    def do_update(self, arg: str):
        """Updates an instance based on the class name and id.
        """
        args = arg.split(maxsplit=3)
        if not validate_classname(args, check_id=True):
            return

        instance_objs = storage.all()
        key = "{}.{}".format(args[0], args[1])
        req_instance = instance_objs.get(key, None)
        if req_instance is None:
            print("** no instance found **")
            return

        match_json = re.findall(r"{.*}", arg)
        if match_json:
            payload = None
            try:
                payload: dict = json.loads(match_json[0])
            except Exception:
                print("** invalid syntax")
                return
            for k, v in payload.items():
                setattr(req_instance, k, v)
            storage.save()
            return
        if not validate_attrs(args):
            return
        first_attr = re.findall(r"^[\"\'](.*?)[\"\']", args[3])
        if first_attr:
            setattr(req_instance, args[2], first_attr[0])
        else:
            value_list = args[3].split()
            setattr(req_instance, args[2], parse_str(value_list[0]))
        storage.save()


def validate_classname(args, check_id=False):
    """Runs checks on args to validate classname entry.
    """
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in current_classes.keys():
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
