# Atlas-AirBnB_clone

## Objectives:
- To write and read JSON file.
- How to create a Python package.
- Serializing and deserializing classes.
- Create a command interpreter in Python using the cmd Module.

Creating and implementing a base console of a Airbnb application. Which allows it to read the users inputs. It allows the Users to input things base on the basemodels pulling information from different class files. The Airbnb console allows the users to
search and filter properties base on personal reference, check to see listing  of properties, the availabilities of properties, manage their profile, and handle errors.

The console is base off of the command interpreter, in which it can serializes and deserializes data structure into formats that can be store, transfer over, restore, or receive data. The command interpreter allows the user to quit the program, return an emptyline, create a specified class, show specific information, deleting specific instance, and update attributes of specific instance.

# Installation:
##### Steps for installation:
```
git clone (https://github.com/KVang2/atlas-AirBnB_clone.git)
```

## How to Start It:
To start the command interpreter, run the file 'console.py' simply by running the script, with (./). Once you run it the prompt '(hbnb)' should appear. It then allows you to imput commands.
```
$ ./console.py
```

```
$ ./console.py
(hbnb)
```

## How to use it:
Once your command interpreter is running, it'll allow you to enter commands to operate the AirBnB console.
#### List of Commands:
- create: Creates new instances.
- show: Displays specified information of an instance.
- destroy: Deletes specified instance. 
- all: Displays information about all instances.
- quit or EOF: Which it exits you out of the command interpreter.
- help: settings that assist you, by giving the command names.
# Testing
To test the files you can run the command:
```
python3 -m unittest discover tests
```
