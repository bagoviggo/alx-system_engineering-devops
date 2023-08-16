# 0x03 Shell Variables and Expansions

Welcome to the Shell Variables and Expansions project directory! In this section, you'll delve into the world of shell variables, expansions, and how they play a crucial role in customizing your shell environment.

## Learning Objectives

By the end of this project, you should be able to:

- Understand shell expansions and their significance.
- Differentiate between single and double quotes and utilize them effectively.
- Perform command substitution using `$()` and backticks.
- Create and manage shell variables, including local and global variables.
- Recognize and utilize reserved variables.
- Understand the roles of reserved variables like `HOME`, `PATH`, and `PS1`.
- Utilize special parameters and understand their purpose.
- Perform arithmetic operations using shell arithmetic.
- Create and manage aliases for commands.

## Resources

Read or watch:

- [Expansions](http://linuxcommand.org/lc3_lts0060.php)
- [Shell Arithmetic](http://linuxcommand.org/lc3_lts0070.php)
- [Variables](http://linuxcommand.org/lc3_lts0080.php)
- [Shell initialization files](http://linuxcommand.org/lc3_lts0090.php)
- [The alias Command](http://linuxcommand.org/lc3_lts0100.php)
- [Technical Writing](https://www.writethedocs.org/guide/writing/beginners-guide-to-docs/)

Man or help:

- `printenv`
- `set`
- `unset`
- `export`
- `alias`
- `unalias`
- `.`
- `source`
- `printf`

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Understand the effects of executing `$ ls -l *.txt`.

### Shell Initialization Files

- Define the roles of `/etc/profile` and `/etc/profile.d` in shell initialization.
- Understand the purpose of the `~/.bashrc` file.

### Variables

- Differentiate between local and global variables.
- Recognize reserved variables and their importance.
- Create, update, and delete shell variables.
- Understand the roles of reserved variables like `HOME`, `PATH`, and `PS1`.
- Utilize special parameters like `?`.

### Expansions

- Define shell expansions and their applications.
- Differentiate between single and double quotes and use them effectively.
- Perform command substitution using `$()` and backticks.

### Shell Arithmetic

- Perform arithmetic operations using shell arithmetic.

### The alias Command

- Create and manage aliases for commands.
- List existing aliases and temporarily disable them.

### Other Help Pages

- Execute commands from a file in the current shell.

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
General

- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`$ wc -l file` should print 2)
- All your files should end with a new line (why?)
- The first line of all your files should be exactly `#!/bin/bash`
- A README.md file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use `&&`, `||`, or `;`
- You are not allowed to use `bc`, `sed`, or `awk`
- All your files must be executable

More Info

Read your `/etc/profile`, `/etc/inputrc`, and `~/.bashrc` files.

Look at some files in the `/etc/profile.d` directory.

Note: You do not have to learn about `awk`, `tar`, `bzip2`, `date`, `scp`, `ulimit`, `umask`, or shell scripting, yet.

## Project List

- [0-alias](./0-alias): Create an alias named `ls` with the value `rm *`.
- [10-love_exponent_breath](./10-love_exponent_breath): Display the result of an exponentiation.
- [11-binary_to_decimal](./11-binary_to_decimal): Convert a binary number to a decimal number.
- [12-combinations](./12-combinations): Display all possible combinations of two letters, except `oo`.
- [13-print_float](./13-print_float): Print a floating point number with two decimal places.
- [1-hello_you](./1-hello_you): Print "Hello user", where user is the current Linux user.
- [2-path](./2-path): Add `/action` to the `PATH`.
- [3-paths](./3-paths): Count the number of directories in the `PATH`.
- [4-global_variables](./4-global_variables): List environment variables.
- [5-local_variables](./5-local_variables): List all local variables and environment variables, and functions.
- [6-create_local_variable](./6-create_local_variable): Create a new local variable.
- [7-create_global_variable](./7-create_global_variable): Create a new global variable.
- [8-true_knowledge](./8-true_knowledge): Print the result of the addition of 128 with the value stored in the environment variable `TRUEKNOWLEDGE`, followed by a new line.
- [9-divide_and_rule](./9-divide_and_rule): Divide 2 numbers and print the result.
- [README.md](./README.md): This README file.

Feel free to explore each project's directory for detailed instructions and exercises related to shell variables and expansions.

## About Shell Variables and Expansions

Shell variables allow you to store and manipulate data for use in your shell environment. Expansions, on the other hand, are mechanisms that allow you to process and manipulate strings, paths, and command outputs directly within commands.

## Getting Started

To begin working on any of the projects, navigate to the individual project directories and follow the instructions provided in the respective README files.

---

Expand your shell skills and harness the power of variables and expansions to enhance your shell experience!
