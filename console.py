#!/usr/bin/python3
"""The entry point of the command interpreter."""

import cmd
import json
import re
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):

    """The command interpreter class"""

    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if there are no matches."""
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
        classname = match.group(1)
        mthd = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False

        attr_and_value = ""
        if mthd == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            match_attr_and_value = re.search(
                '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)
            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(
                    1) or "") + " " + (match_attr_and_value.group(2) or "")
        command = mthd + " " + classname + " " + uid + " " + attr_and_value
        self.onecmd(command)
        return command

    def update_dict(self, classname, uid, s_dict):
        """The helper method for update() with a dictionary"""
        i = s_dict.replace("'", '"')
        a = json.loads(i)
        if not classname:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            else:
                attributes = storage.attributes()[classname]
                for attribute, value in a.items():
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
        """Handles End Of File(E0F) character"""
        print()
        return True

    def do_quit(self, line):
        """Exits the program"""
        return True

    def emptyline(self):
        """This does nothing on ENTER"""
        pass

    def do_create(self, line):
        """Creates a new instance"""

        if line == "" or line is None:
            print("** class name missing **")

        elif line not in storage.classes():
            print("** class doesn't exist **")

        else:
            i = storage.classes()[line]()
            i.save()
            print(i.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if line == "" or line is None:
            print("** class name missing **")

        else:
            words = line.split(' ')

            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(words) < 2:
                print("** instance id missing **")

            else:
                key = "{}.{}".format(words[0], words[1])

                if key not in storage.all():
                    print("** no instance found **")

                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == "" or line is None:
            print("** class name missing **")

        else:
            words = line.split(' ')

            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            elif len(words) < 2:
                print("** instance id missing **")

            else:
                key = "{}.{}".format(words[0], words[1])

                if key not in storage.all():
                    print("** no instance found **")

                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """This prints all string representation of all instances.
        """
        if line != "":
            words = line.split(' ')

            if words[0] not in storage.classes():
                print("** class doesn't exist **")

            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_count(self, line):
        """This counts the instances of a class.
        """
        words = line.split(' ')
        if not words[0]:
            print("** class name missing **")

        elif words[0] not in storage.classes():
            print("** class doesn't exist **")

        else:
            matches = [
                k for k in storage.all() if k.startswith(
                    words[0] + '.')]
            print(len(matches))

    def do_update(self, line):
        """Updates an instance by adding or updating attribute"""
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")

        elif classname not in storage.classes():
            print("** class doesn't exist **")

        elif uid is None:
            print("** instance id missing **")

        else:
            key = "{}.{}".format(classname, uid)

            if key not in storage.all():
                print("** no instance found **")

            elif not attribute:
                print("** attribute name missing **")

            elif not value:
                print("** value missing **")

            else:
                cast = None
                if not re.search('^".*"$', value):

                    if '.' in value:
                        cast = float

                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)

                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
