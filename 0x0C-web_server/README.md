# 0x0C Web Server

Welcome to the Web Server project directory! In this section, you'll delve into the world of web servers and configuration. You'll learn how to set up, configure, and manage web servers to host websites and web applications.

## Background Context

This project emphasizes the automation of tasks through scripting and configuration. You'll learn to configure your web-01 server according to requirements and create Bash scripts that automate the setup process. Automating tasks allows you to streamline repetitive work and focus on more exciting challenges.

For instance, if you need to create a file `/tmp/test` containing the string "hello world" and modify the configuration of Nginx to listen on port 8080 instead of 80, you can use a Bash script to perform these tasks. This exercise aims to train you in automating manual tasks, a valuable skill for managing large numbers of servers.

Remember that the checker will execute your script as the root user, so you don't need to use the `sudo` command.

A good Software Engineer is a lazy Software Engineer.

## Resources

Read or watch:

- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://www.nginx.com/resources/glossary/nginx/)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-configure-nginx)
- [Child process concept page](https://en.wikipedia.org/wiki/Child_process)
- [Root and subdomain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-subdomain/)
- [HTTP requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)
- [HTTP redirection](https://developer.mozilla.org/en-US/docs/Web/HTTP/Redirections)
- [Not found HTTP response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/404)
- [Logs files on Linux](https://www.digitalocean.com/community/tutorials/how-to-view-and-configure-linux-logs-on-ubuntu-and-centos)

For reference:

- [RFC 7231 (HTTP/1.1)](https://tools.ietf.org/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://tools.ietf.org/html/rfc7540)

Man or help:

- `scp`
- `curl`

## Learning Objectives

By the end of this project, you are expected to be able to explain the following topics to anyone, without the help of Google:

### General

- Understand the main role of a web server.
- Define what a child process is.
- Explain why web servers usually have a parent process and child processes.
- Identify the main HTTP requests.

### DNS

- Define what DNS stands for.
- Understand the main role of DNS.

### DNS Record Types

- Explain the purpose of DNS record types A, CNAME, TXT, MX.

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing
- You can't use systemctl for restarting a process

