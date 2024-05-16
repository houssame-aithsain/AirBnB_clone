#!/usr/bin/python3
# the console for the AirBnB project

import re
import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for Holberton AirBnB project"""
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel, save it and print the id"""
        if not line:
            print("** class name missing **")
        elif line not in storage.classes:
            print("** class doesn't exist **")
        else:
            new_instance = storage.classes[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id (save the change into the JSON file)"""
    
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print("** no instance found **")
        
    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        args = line.split()
        if not line:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in storage.all().items() if key.split('.')[0] == args[0]])
    
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in storage.all():
                setattr(storage.all()[key], args[2], args[3])
                storage.all()[key].save()
            else:
                print("** no instance found **")
    
    def do_count(self, line):
        """Retrieve the number of instances of a class"""
        count = 0
        args = line.split()
        if args[0] not in storage.classes:
            print("** class doesn't exist **")
        else:
            for key in storage.all():
                if key.split('.')[0] == args[0]:
                    count += 1
            print(count)

    def default(self, line):
        """Called on an input line when the command prefix is not recognized"""
        args = line.split('.')
        if len(args) > 1:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.do_count(args[0])
            elif args[1][:4] == "show":
                match = re.match(r'show\(([^)]*)\)', args[1])
                if match:
                    self.do_show(args[0] + " " + match.group(1))
            elif args[1][:7] == "destroy":
                match = re.match(r'destroy\(([^)]*)\)', args[1])
                if match:
                    self.do_destroy(args[0] + " " + match.group(1))
            elif args[1][:6] == "update":
                match = re.match(r'update\(([^)]*)\)', args[1])
                if match:
                    self.do_update(args[0] + " " + match.group(1))
        else:
            print("*** Unknown syntax: {}".format(line))
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
