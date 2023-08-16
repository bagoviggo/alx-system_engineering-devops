# 0x00 Shell Basics

Welcome to the Shell Basics project directory! This section covers fundamental concepts of using the command-line interface (CLI) in a Unix-like environment. Each project focuses on different aspects of navigating directories, manipulating files, and executing commands.

## Learning Objectives

At the end of this project, you are expected to be able to explain the following topics to anyone, without the help of Google:

### General

- What does _RTFM_ mean?
- What is a _Shebang_?

### What is the Shell

- What is the shell?
- What is the difference between a terminal and a shell?
- What is the shell prompt?
- How to use the history (the basics).

### Navigation

- What do the commands or built-ins `cd`, `pwd`, `ls` do?
- How to navigate the filesystem.
- What are the `.`, and `..` directories?
- What is the working directory, how to print it and how to change it?
- What is the root directory?
- What is the home directory, and how to go there?
- What is the difference between the root directory and the home directory of the user root?
- What are the characteristics of hidden files and how to list them?
- What does the command `cd -` do?

### Looking Around

- What do the commands `ls`, `less`, `file` do?
- How do you use options and arguments with commands?
- Understand the `ls` long format and how to display it.
- A Guided Tour.
- What does the `ln` command do?
- What do you find in the most common/important directories?
- What is a symbolic link?
- What is a hard link?
- What is the difference between a hard link and a symbolic link?

### Manipulating Files

- What do the commands `cp`, `mv`, `rm`, `mkdir` do?
- What are wildcards and how do they work?
- How to use wildcards?

### Working with Commands

- What do `type`, `which`, `help`, `man` commands do?
- What are the different kinds of commands?
- What is an alias?
- When do you use the command `help` instead of `man`?

### Reading Man Pages

- How to read a man page.
- What are man page sections?
- What are the section numbers for User commands, System calls, and Library functions?

### Keyboard Shortcuts for Bash

- Common shortcuts for Bash.

## Project List

- [0-current_working_directory](./0-current_working_directory): Print the current working directory using the `pwd` command.
- [100-lets_move](./100-lets_move): Move a file to a different location in the file system using the `mv` command.
- [101-clean_emacs](./101-clean_emacs): Clean up backup files created by Emacs using shell commands.
- [102-tree](./102-tree): Create a tree-like directory structure using shell commands.
- [103-commas](./103-commas): List files and directories in a comma-separated format using shell commands.
- [10-back](./10-back): Navigate to the previous directory using the `cd` command.
- [11-lists](./11-lists): List all files, including hidden ones, in the current directory using the `ls` command.
- [12-file_type](./12-file_type): Display the type of a file using the `file` command.
- [13-symbolic_link](./13-symbolic_link): Create a symbolic link using the `ln` command.
- [14-copy_html](./14-copy_html): Copy all HTML files from the current directory to a target directory using the `cp` command.
- ... (and so on for the rest of the projects)

Feel free to explore each project's directory for detailed instructions and exercises related to shell basics.


## Getting Started

To get started with any of the projects, navigate to the individual project directories and follow the instructions provided in the respective README files.

---

- ### Requirements
    #### General

    - Allowed editors: vi, vim, emacs
    - All your scripts will be tested on Ubuntu 20.04 LTS
    - All your scripts should be exactly two lines long ($ wc -l file should print 2)
    - All your files should end with a new line (why?)
    - The first line of all your files should be exactly #!/bin/bash
    - A README.md file at the root of the repo, containing a description of the repository
    - A README.md file, at the root of the folder of this project, describing what each script is doing
    - You are not allowed to use backticks, &&, || or ;
    - All your scripts must be executable. To make your file executable, use the chmod command: chmod u+x file. Later, we’ll learn more about how to utilize this command.



