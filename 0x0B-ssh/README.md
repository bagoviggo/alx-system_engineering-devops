# 0x0B SSH

Welcome to the SSH (Secure Shell) project directory! In this section, you'll explore concepts related to secure remote access and management of systems using SSH.

<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/244/zPVRKhPsUP5lK.gif" alt="Man Dancing Gif" width="600" height="400">


## Background Context

In this project, you've been attributed an Ubuntu server, living in a distant datacenter. Unlike the previous level, you'll connect using SSH but not with a password; rather, you'll use an RSA key. The server has already been configured with the public key you created in the first task of a previous project, which is shared in your intranet profile.

You can access your server information in the "My Servers" section of the intranet. Each line contains the IP address and username to use for SSH connections.

**Note:** Your server is configured with an Ubuntu 20.04 LTS environment.

## Resources

Read or watch:

- [What is a (physical) server - text](https://en.wikipedia.org/wiki/Server_(computing))
- [What is a (physical) server - video](https://www.youtube.com/watch?v=_3UN4aP4okw)
- [SSH essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-the-basics)
- [SSH Config File](https://www.ssh.com/academy/ssh/config)
- [Public Key Authentication for SSH](https://www.ssh.com/academy/ssh/public-key-authentication)
- [How Secure Shell Works](https://www.ssh.com/academy/ssh)
- [SSH Crash Course](https://www.youtube.com/watch?v=hQWRp-FdTpc) (Long, but highly informative. Watch at x1.25 speed or above.)

For reference:

- [Understanding the SSH Encryption and Connection Process](https://www.digitalocean.com/community/tutorials/understanding-the-ssh-encryption-and-connection-process)
- [Secure Shell Wiki](https://en.wikipedia.org/wiki/Secure_Shell)
- [IETF RFC 4251 (Description of the SSH Protocol)](https://tools.ietf.org/html/rfc4251)
- [Internet Engineering Task Force](https://www.ietf.org/)
- [Request for Comments](https://www.rfc-editor.org/)

Man or help:

- `ssh`
- `ssh-keygen`
- `env`

## Learning Objectives

By the end of this project, you are expected to be able to explain the following topics to anyone, without the help of Google:

### General

- What is a server?
- Where do servers usually reside?
- What is SSH?
- How to create an SSH RSA key pair.
- How to connect to a remote host using an SSH RSA key pair.
- The advantage of using `#!/usr/bin/env bash` instead of `/bin/bash`.

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

