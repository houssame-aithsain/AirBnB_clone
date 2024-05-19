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
    """ command interpreter """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """emptyline method"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        elif arg not in cClass:
            print("** class doesn't exist **")
        else:
            new = cClass[arg]()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] not in cClass:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                key = arg[0] + '.' + arg[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] not in cClass:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                key = arg[0] + '.' + arg[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(v) for v in storage.all().values()])
        elif arg not in cClass:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if arg in k])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] not in cClass:
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id missing **")
            else:
                key = arg[0] + '.' + arg[1]
                if key not in storage.all():
                    print("** no instance found **")
                elif len(arg) < 3:
                    print("** attribute name missing **")
                elif len(arg) < 4:
                    print("** value missing **")
                else:
                    setattr(storage.all()[key], arg[2], arg[3])
                    storage.all()[key].save()

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        count = 0
        for k in storage.all():
            if arg in k:
                count += 1
        print(count)

    def default(self, arg):
        """default method"""
        args = arg.split('.')
        if len(args) > 1:
            if args[1] == 'all()':
                self.do_all(args[0])
            elif args[1] == 'count()':
                self.do_count(args[0])
            elif args[1][:4] == 'show':
                self.do_show(args[0] + ' ' + args[1][6:-2])
            elif args[1][:7] == 'destroy':
                self.do_destroy(args[0] + ' ' + args[1][9:-2])
            elif args[1][:6] == 'update':
                args[1] = args[1][8:-2]
                args[1] = args[1].replace(',', '')
                self.do_update(args[0] + ' ' + args[1])
        else:
            cmd.Cmd.default(self, arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
