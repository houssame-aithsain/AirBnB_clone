#!/usr/bin/python3
"""Command interpreter for the HBNB project."""

import re
import cmd
import json
from models import storage
from models.base_model import BaseModel

available_classes = {
    'BaseModel': BaseModel
}

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the HBNB project."""

    prompt = "(hbnb) "

    def precmd(self, line):
        """Modify command line before interpreting it."""
        if not line:
            return '\n'

        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        matches = pattern.findall(line)
        if not matches:
            return super().precmd(line)

        match = matches[0]
        if not match[2]:
            if match[1] == "count":
                instances = storage.all()
                print(len([
                    obj for obj in instances.values()
                    if type(obj).__name__ == match[0]
                ]))
                return "\n"
            return f"{match[1]} {match[0]}"
        else:
            args = match[2].split(", ")
            if len(args) == 1:
                return "{} {} {}".format(
                    match[1], match[0],
                    re.sub("[\"\']", "", match[2]))
            else:
                json_match = re.findall(r"{.*}", match[2])
                if json_match:
                    return "{} {} {} {}".format(
                        match[1], match[0],
                        re.sub("[\"\']", "", args[0]),
                        json_match[0])
                return "{} {} {} {}".format(
                    match[1], match[0],
                    re.sub("[\"\']", "", args[0]),
                    re.sub("[\"\']", "", args[1]))

    def do_help(self, arg):
        """Get help on a command."""
        return super().do_help(arg)

    def do_EOF(self, line):
        """Handle EOF to gracefully exit."""
        print("")
        return True

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def emptyline(self):
        """Override default behavior of executing the last command."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class."""
        args = arg.split()
        if not validate_class_name(args):
            return

        new_instance = available_classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not validate_class_name(args, check_id=True):
            return

        instances = storage.all()
        instance_key = f"{args[0]}.{args[1]}"
        instance = instances.get(instance_key)
        if instance is None:
            print("** no instance found **")
            return
        print(instance)

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = arg.split()
        if not validate_class_name(args, check_id=True):
            return

        instances = storage.all()
        instance_key = f"{args[0]}.{args[1]}"
        instance = instances.get(instance_key)
        if instance is None:
            print("** no instance found **")
            return

        del instances[instance_key]
        storage.save()

    def do_all(self, arg):
        """Print the string representation of all instances."""
        args = arg.split()
        all_instances = storage.all()

        if len(args) < 1:
            print([str(obj) for obj in all_instances.values()])
            return
        if args[0] not in available_classes:
            print("** class doesn't exist **")
            return
        else:
            print([str(obj) for obj in all_instances.values() if type(obj).__name__ == args[0]])
            return

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = arg.split(maxsplit=3)
        if not validate_class_name(args, check_id=True):
            return

        instances = storage.all()
        instance_key = f"{args[0]}.{args[1]}"
        instance = instances.get(instance_key)
        if instance is None:
            print("** no instance found **")
            return

        json_match = re.findall(r"{.*}", arg)
        if json_match:
            try:
                attributes = json.loads(json_match[0])
            except json.JSONDecodeError:
                print("** invalid syntax **")
                return
            for key, value in attributes.items():
                setattr(instance, key, value)
            storage.save()
            return
        if not validate_attributes(args):
            return
        attr_name = re.findall(r'^[\"\'](.*?)[\"\']', args[3])
        if attr_name:
            setattr(instance, args[2], attr_name[0])
        else:
            value = args[3].split()
            setattr(instance, args[2], parse_value(value[0]))
        storage.save()

def validate_class_name(args, check_id=False):
    """Validate the class name."""
    if len(args) < 1:
        print("** class name missing **")
        return False
    if args[0] not in available_classes:
        print("** class doesn't exist **")
        return False
    if len(args) < 2 and check_id:
        print("** instance id missing **")
        return False
    return True

def validate_attributes(args):
    """Validate the attributes."""
    if len(args) < 3:
        print("** attribute name missing **")
        return False
    if len(args) < 4:
        print("** value missing **")
        return False
    return True

def is_float(value):
    """Check if a value is a float."""
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False

def is_integer(value):
    """Check if a value is an integer."""
    try:
        return float(value).is_integer()
    except (TypeError, ValueError):
        return False

def parse_value(value):
    """Parse a string value into an integer, float, or string."""
    cleaned_value = re.sub(r'"', '', value)

    if is_integer(cleaned_value):
        return int(cleaned_value)
    elif is_float(cleaned_value):
        return float(cleaned_value)
    else:
        return value

if __name__ == "__main__":
    HBNBCommand().cmdloop()
