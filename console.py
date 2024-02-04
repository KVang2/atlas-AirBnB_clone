#!/usr/bin/python3
"""
Program that contains entry point of command interpreter:
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit program on EOF"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def create(self, arg):
        """create"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
