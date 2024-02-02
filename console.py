#!/usr/bin/python3
"""
Program that contains entry point of command interpreter:
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter"""
    intro = "Welcome to the command interpreter. Type 'help' for a list of commands."
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        return True
    
    def do_EOF(self, arg):
        """Exit the program on EOF"""
        return True
    
    def do_help(self, arg):
        """Show informations"""
        super().do_help(arg)

    def emptylin(self):
        """Empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
