markdown

# AirBnB Clone - ALX Project

## Description

The AirBnB Clone project is a collaborative software engineering endeavor as part of the ALX SE program. It aims to teach students the fundamentals of full-stack web development by recreating an Airbnb-like platform. This project is divided into multiple phases, starting with the creation of a command-line interface (CLI) for managing application data, and progressing towards a complete web application.

## Command Interpreter

The command interpreter is a crucial component of the AirBnB Clone project. It allows users to interact with the application through a CLI, performing various operations on the data models, such as creating, updating, deleting, and retrieving objects.

### How to Start the Command Interpreter

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/houssame-aithsain/AirBnB_clone.git

    Navigate to the Project Directory:

    bash

cd AirBnB_clone

Run the Console:

bash

    ./console.py

How to Use the Command Interpreter

The command interpreter supports several commands to manage the application's data models. These commands can be executed in both interactive and non-interactive modes.
Interactive Mode

In interactive mode, you start the interpreter and then type commands at the (hbnb) prompt.

bash

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) create User
d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3
(hbnb) show User d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3
[User] (d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3) {'id': 'd3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3', 'created_at': '2023-05-19T12:00:00', 'updated_at': '2023-05-19T12:00:00'}
(hbnb) quit

Non-Interactive Mode

In non-interactive mode, you can pipe commands directly into the interpreter from the shell.

bash

$ echo "create User" | ./console.py
(hbnb) d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3
$ echo "show User d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3" | ./console.py
[User] (d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3) {'id': 'd3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3', 'created_at': '2023-05-19T12:00:00', 'updated_at': '2023-05-19T12:00:00'}

Command Usage Examples

Here are some examples of how to use the command interpreter:

    Create a new object:

    bash

(hbnb) create User
d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3

Show an object:

bash

(hbnb) show User d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3
[User] (d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3) {'id': 'd3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3', 'created_at': '2023-05-19T12:00:00', 'updated_at': '2023-05-19T12:00:00'}

Update an object:

bash

(hbnb) update User d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3 name "Alice"

Delete an object:

bash

(hbnb) destroy User d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3

Show all objects:

bash

(hbnb) all User
["[User] (d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3) {'id': 'd3f029a3-675d-4f7d-9b3a-3d61
