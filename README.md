<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>AirBnB Clone - ALX Project</h1>
    
    <h2>Description</h2>
    <p>The AirBnB Clone project is a collaborative software engineering endeavor as part of the ALX SE program. It aims to teach students the fundamentals of full-stack web development by recreating an Airbnb-like platform. This project is divided into multiple phases, starting with the creation of a command-line interface (CLI) for managing application data, and progressing towards a complete web application.</p>
    
    <h2>Command Interpreter</h2>
    <p>The command interpreter is a crucial component of the AirBnB Clone project. It allows users to interact with the application through a CLI, performing various operations on the data models, such as creating, updating, deleting, and retrieving objects.</p>
    
    <h3>How to Start the Command Interpreter</h3>
    <ol>
        <li><strong>Clone the Repository</strong>:
            <pre><code>git clone https://github.com/houssame-aithsain/AirBnB_clone.git</code></pre>
        </li>
        <li><strong>Navigate to the Project Directory</strong>:
            <pre><code>cd AirBnB_clone</code></pre>
        </li>
        <li><strong>Run the Console</strong>:
            <pre><code>./console.py</code></pre>
        </li>
    </ol>
    
    <h3>How to Use the Command Interpreter</h3>
    <p>The command interpreter supports several commands to manage the application's data models. These commands can be executed in both interactive and non-interactive modes.</p>
    
    <h4>Interactive Mode</h4>
    <p>In interactive mode, you start the interpreter and then type commands at the <code>(hbnb)</code> prompt.</p>
    <pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) create User
d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3
(hbnb) show User d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3
[User] (d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3) {'id': 'd3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3', 'created_at': '2023-05-19T12:00:00', 'updated_at': '2023-05-19T12:00:00'}
(hbnb) quit</code></pre>
    
    <h4>Non-Interactive Mode</h4>
    <p>In non-interactive mode, you can pipe commands directly into the interpreter from the shell.</p>
    <pre><code>$ echo "create User" | ./console.py
(hbnb) d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3
$ echo "show User d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3" | ./console.py
[User] (d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3) {'id': 'd3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3', 'created_at': '2023-05-19T12:00:00', 'updated_at': '2023-05-19T12:00:00'}</code></pre>
    
    <h3>Command Usage Examples</h3>
    <p>Here are some examples of how to use the command interpreter:</p>
    <ul>
        <li><strong>Create a new object</strong>:
            <pre><code>(hbnb) create User
d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3</code></pre>
        </li>
        <li><strong>Show an object</strong>:
            <pre><code>(hbnb) show User d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3
[User] (d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3) {'id': 'd3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3', 'created_at': '2023-05-19T12:00:00', 'updated_at': '2023-05-19T12:00:00'}</code></pre>
        </li>
        <li><strong>Update an object</strong>:
            <pre><code>(hbnb) update User d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3 name "Alice"</code></pre>
        </li>
        <li><strong>Delete an object</strong>:
            <pre><code>(hbnb) destroy User d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3</code></pre>
        </li>
        <li><strong>Show all objects</strong>:
            <pre><code>(hbnb) all User
["[User] (d3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3) {'id': 'd3f029a3-675d-4f7d-9b3a-3d61b0b0b2c3', 'created_at': '2023-05-19T12:00:00', 'updated_at': '2023-05-19T12:00:00', 'name': 'Alice'}"]</code></pre>
        </li>
    </ul>
    
    <p>For more details, refer to the project documentation and code comments. Happy coding!</p>
</body>
</html>
