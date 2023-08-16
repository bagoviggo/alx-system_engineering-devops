# 0x02 Shell Redirection

Welcome to the Shell Redirection project directory! In this section, you'll explore the powerful concept of shell redirection and how it can be used to manage input and output streams of commands in the terminal.

## Learning Objectives

By the end of this project, you should be able to:

- Understand and apply shell redirection concepts.
- Redirect input and output streams using various symbols.
- Combine multiple commands and redirect their input/output.
- Manipulate text files using redirection.
- Utilize redirection for filtering and processing data.

## Resources

Read or watch:

- [Shell, I/O Redirection](http://linuxcommand.org/lc3_lts0070.php)
- [Special Characters](http://linuxcommand.org/lc3_lts0080.php)

Man or help:

- `echo`
- `cat`
- `head`
- `tail`
- `find`
- `wc`
- `sort`
- `uniq`
- `grep`
- `tr`
- `rev`
- `cut`
- `passwd` (5) (i.e., `man 5 passwd`)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### Shell, I/O Redirection

- Understand the purpose of commands `head`, `tail`, `find`, `wc`, `sort`, `uniq`, `grep`, `tr`.
- Redirect standard output to a file.
- Get standard input from a file instead of the keyboard.
- Send the output from one program to the input of another program.
- Combine commands and filters with redirections.

### Special Characters

- Define and identify special characters.
- Understand and use white spaces, single quotes, double quotes, backslash, comment, pipe, command separator, and tilde.

### Other Man Pages

- Display a line of text.
- Concatenate files and print on the standard output.
- Reverse a string.
- Remove sections from each line of files.
- Understand the format of the `/etc/passwd` file.
- Understand the format of the `/etc/shadow` file.

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
General

- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long ($ wc -l file should print 2)
- All your files should end with a new line (why?)
- The first line of all your files should be exactly `#!/bin/bash`
- A README.md file, at the root of the folder of the project, describing what each script is doing
- You are not allowed to use backticks, &&, ||, or ;
- All your files must be executable
- You are not allowed to use `sed` or `awk`

More Info

Read your `/etc/passwd` and `/etc/shadow` files.

Note: You do not have to learn about `fmt`, `pr`, `du`, `gzip`, `tar`, `lpr`, `sed`, and `awk` yet.

## Project List

- [0-hello_world](./0-hello_world): Display "Hello, World" using the `echo` command.
- [100-empty_casks](./100-empty_casks): Create an empty file called `casks`.
- [101-gifs](./101-gifs): List all the files with a `.gif` extension in the current directory and its subdirectories.
- [102-acrostic](./102-acrostic): Display an acrostic using heredoc syntax.
- [103-the_biggest_fan](./103-the_biggest_fan): Create a file named `text` with specific content.
- [10-no_more_js](./10-no_more_js): Delete all files with a `.js` extension in the current directory and its subdirectories.
- [11-directories](./11-directories): Count the number of directories and sub-directories.
- [12-newest_files](./12-newest_files): Display the 10 newest files in the current directory.
- [13-unique](./13-unique): Print only words that appear exactly once from a list.
- [14-findthatword](./14-findthatword): Display lines containing the pattern "root" from a text file.
- [15-countthatword](./15-countthatword): Display the number of lines that contain the pattern "bin" in a text file.
- [16-whatsnext](./16-whatsnext): Display lines containing the pattern "root" and the three lines after them.
- [17-hidethisword](./17-hidethisword): Display all lines from a text file that do not contain the pattern "bin".
- [18-letteronly](./18-letteronly): Display only letters from a text file.
- [19-AZ](./19-AZ): Replace all characters A and c from input to Z and e, respectively.
- [1-confused_smiley](./1-confused_smiley): Display a confused smiley `"(Ôo)'` to the terminal.
- [20-hiago](./20-hiago): Remove all letters `c` and `C` from input.
- [21-reverse](./21-reverse): Reverse the input.
- [22-users_and_homes](./22-users_and_homes): Display all users and their home directories.
- [2-hellofile](./2-hellofile): Display the content of a file.
- [3-twofiles](./3-twofiles): Display the content of two files.
- [4-lastlines](./4-lastlines): Display the last 10 lines of a file.
- [5-firstlines](./5-firstlines): Display the first 10 lines of a file.
- [6-third_line](./6-third_line): Display the third line of a file.
- [7-file](./7-file): Create a file with a specific content.
- [8-cwd_state](./8-cwd_state): Write into a file the result of `ls -la`.
- [9-duplicate_last_line](./9-duplicate_last_line): Duplicate the last line of a file.
- [README.md](./README.md): This file.


Feel free to explore each project's directory for detailed instructions and exercises related to shell redirection.

## About Shell Redirection

Shell redirection allows you to control the flow of data between commands and files. By using redirection operators, you can redirect input, output, and error streams to and from files, making it a powerful tool for text processing and data manipulation.

## Getting Started

To get started with any of the projects, navigate to the individual project directories and follow the instructions provided in the respective README files.

---

Happy learning and mastering the art of shell redirection!
