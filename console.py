#!/usr/bin/python3
"""The entry point of the command interpreter."""

import cmd
import json
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
<<<<<<< HEAD
        """Catch commands if nothing else matches then."""
=======
        """Catch commands if there are no matches."""
>>>>>>> 92558bf85f1145e57f27a95f10d6c01c63579c2f
        self._precmd(line)

    def _precmd(self, line):
        """Intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", line)
        if not match:
            return line
<<<<<<< HEAD
        classname, method, args = match.groups()
=======
        classname = match.group(1)
        mthd = match.group(2)
        args = match.group(3)
>>>>>>> 92558bf85f1145e57f27a95f10d6c01c63579c2f
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        uid, attr_or_dict = match_uid_and_args.groups() if match_uid_and_args else (args, None)

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
<<<<<<< HEAD
        command = f"{method} {classname} {uid} {attr_and_value}"
=======
        command = mthd + " " + classname + " " + uid + " " + attr_and_value
>>>>>>> 92558bf85f1145e57f27a95f10d6c01c63579c2f
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
            key = f"{classname}.{uid}"
            if key not in storage.all():
                print("** no instance found **")
            else:
<<<<<<< HEAD
                attributes = storage.attributes().get(classname, {})
                for attribute, value in d.items():
=======
                attributes = storage.attributes()[classname]
                for attribute, value in a.items():
>>>>>>> 92558bf85f1145e57f27a95f10d6c01c63579c2f
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()

    def do_EOF(self, line):
<<<<<<< HEAD
        """This handles End Of File character."""
=======
        """Handles End Of File(E0F) character"""
>>>>>>> 92558bf85f1145e57f27a95f10d6c01c63579c2f
        print()
        return True

    def do_quit(self, line):
<<<<<<< HEAD
        """This exits the program."""
        return True

    def emptyline(self):
        """This doesn't do anything on ENTER."""
        pass

    def do_create(self, line):
        """This creates an instance."""
        if not line:
=======
        """Exits the program"""
        return True

    def emptyline(self):
        """This does nothing on ENTER"""
        pass

    def do_create(self, line):
        """Creates a new instance"""

        if line == "" or line is None:
>>>>>>> 92558bf85f1145e57f27a95f10d6c01c63579c2f
            print("** class name missing **")

        elif line not in storage.classes():
            print("** class doesn't exist **")

        else:
<<<<<<< HEAD
            new_instance = storage.classes()[line]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """This prints the string representation of an instance."""
        words = line.split()
        if not line or not words:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance id missing **")
        else:
            key = f"{words[0]}.{words[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """This deletes an instance based on the class name and id."""
        words = line.split()
        if not line or not words:
            print("** class name missing **")
        elif words[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(words) < 2:
            print("** instance id missing **")
        else:
            key = f"{words[0]}.{words[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """This prints all string representation of all instances."""
        if line:
            words = line.split()
            if not words or words[0] not in storage.classes():
=======
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
>>>>>>> 92558bf85f1145e57f27a95f10d6c01c63579c2f
                print("** class doesn't exist **")

            else:
                instances = [str(obj) for key, obj in storage.all().items()
                             if type(obj).__name__ == words[0]]
                print(instances)
        else:
            instances = [str(obj) for key, obj in storage.all().items()]
            print(instances)

    def do_count(self, line):
        """This counts the instances of a class."""
        words = line.split()
        if not line or not words or not words[0]:
            print("** class name missing **")

        elif words[0] not in storage.classes():
            print("** class doesn't exist **")

        else:
            count = sum(1 for k in storage.all() if k.startswith(f"{words[0]}."))
            print(count)

    def do_update(self, line):
<<<<<<< HEAD
        """This updates an instance by adding or updating attribute."""
        match = re.search(r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?', line)
        if not match:
=======
        """Updates an instance by adding or updating attribute"""
        if line == "" or line is None:
>>>>>>> 92558bf85f1145e57f27a95f10d6c01c63579c2f
            print("** class name missing **")
            return

        classname, uid, attribute, value = match.groups()
        if not classname:
            print("** class name missing **")

        elif classname not in storage.classes():
            print("** class doesn't exist **")
<<<<<<< HEAD
        elif not uid:
=======

        elif uid is None:
>>>>>>> 92558bf85f1145e57f27a95f10d6c01c63579c2f
            print("** instance id missing **")

        else:
<<<<<<< HEAD
            key = f"{classname}.{uid}"
=======
            key = "{}.{}".format(classname, uid)

>>>>>>> 92558bf85f1145e57f27a95f10d6c01c63579c2f
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
                attributes = storage.attributes().get(classname, {})
                if attribute in attributes:
                    value = attributes[attribute](value)

                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
