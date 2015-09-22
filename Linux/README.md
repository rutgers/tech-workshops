# Rutgers IEEE Student Branch - Linux Workshop

## Workshop Leaders

Revan Sopher, Jeremy Savarin

## Module 0 - Setup

Installing Linux takes a while and can get complicated, so we've set up a Linux
server to play around on. If you've already installed Linux or you have a Mac,
you can do this workshop on your own computer instead of the server, but I
recommend using the server to make sure you don't delete anything important.

Usernames and passwords will be distributed in person. Once you get your login
info, on Linux or OS X open the terminal and enter
`ssh username@159.203.76.40`, where `username` is the username we give you.
Type `y` and hit Enter when it warns you that it's never seen this server before.
Type the password when prompted, then hit Enter.

If you're running Windows, there's an additional step because the Windows
terminal doesn't come with the `ssh` program. (Side note: check out
[Babun](http://babun.github.io/index.html) later, a better Windows terminal)
To get started fast,
[download `PuTTY`](http://the.earth.li/~sgtatham/putty/latest/x86/putty.exe).
It's a one-file SSH client that doesn't even need installing -- just run the file.
Fill in the `Host Name` field with `159.203.76.40`, then click `Open`. Hit `Yes`
to the warning about never having seen this server before, then type in the
username and password when prompted.


## Module 1 - Navigating the File System

### 1a. The Linux Filesystem

Here are some of the most important directores in the Linux filesystem:

| Directory         | Function                                      |
| ----------------- | --------------------------------------------- |
| `/`               | root, all directories descend from this       |
| `/bin`            | contains system binaries or programs          |
| `/boot`           | contains Linux kernel and bootloader          |
| `/dev`            | contains device nodes                         |
| `/etc`            | contains system config files                  |
| `/home` or `~`    | only dir where ordinary users can write files |
| `/media`          | mount points for removable media (USB drives) |
| `/opt`            | used to install optional software             |
| `/usr`            | all programs used by regular users            |

### 1b. Moving Around and Making Discoveries

#### Finding about the Current Directory

* `pwd` - print working directory
* `ls` - list files and directories in the working directory

The `ls` command has some useful additional flags you can pass depending on the
output that you want:

* `-l` - display results in long format
* `-a` - include all files including hidden files (begin with . in the
      filename)
* `-h` - display filesizes in human readable format (eg. 4K) vs in bytes
* `-r` - display results in reverse order
* `-t` - sort by last modified time`

You can use multiple flags at once, as in the command `ls -lha`. This will
list all files in long format with their sizes displayed in human readable
format.

#### Moving to Other Directories

* `cd <dir>` - change current working directory to *dir*

For this section, here is some useful notation to know:
* `/` - the root directory
* `~` - the home directory
* `.` - the current directory
* `..` - the parent directory

You don't have to be in a certain directory to list the directory's contents. You can list any directory's contents with:
* `ls <dir>` - list files in directories of *dir*

You can also get information about any file you encounter. Use the following commands:
* `file <file>` - get information about *file's* type
* `less </path/to/file>` - view contents of a file

Play around, and remember! If you ever get lost, remember these key shortcuts!
* `cd` - (no arguments) return to home directory
* `cd -` - return to previous directory
* `cd ..` - return to parent directory

## Module 2 - File/Directory Manipulation

* `mkdir <dir1> <dir2> ... <dirN>` - make directories *dir1* to *dirN*
* `cp` - copy files or directories
* `mv` - move or rename files or directories

The `cp` command has two main uses:
* `cp` <file1> <file2> - copy file/directory *item1* to *item2*
* `cp <file1> <file2> ... <fileN> <dir>` - copy files *file1* to *fileN* to
  directory *dir*

Likewise, the `mv` command has two main uses:
* `mv <item1> <item2>` - rename file/directory *item1* to *item2*
* `mv <file1> <file2> ... <fileN> <dir>` - move files *file1* to *fileN* to
  directory *dir*

Some of the useful options for `cp` are:
* `-i` - prompt user before overwriting files (normally does silent overwriting)
* `-r` - recursively copy directory and contents (needed if copying directories)
* `-u` - only copy files not in target directory or newer than ones in target
  directory
* `-v` - show messages to terminal while copy operation occurs

* `rm` - remove files/directories

Many of the options for `cp` also carry over to the `mv` command.

Options for the `rm` command:
* `-i` - prompt user before deleting file
* `-r` - recursively remove files (need for removing directories)
* `-f` - force removal of file (overrides `-i` flag)
* `-v` - show messages to terminal during remove operation

## Module 3 - Command Information and Manpages

* `type <command>` - display a command's type
* `which <command>` - display an **executable's** location (will not work on
shell built-ins)

There are actually different types of commands:
* executables
* shell built-in commands (`cd`)
* shell functions
* alias - user-defined command built from other commands

### Command Documentation

* `help <command>` - get help on shell built-in command
* `<command> --help` - get help on an executable command
* `man <command>` - show a program's manual/man page 

A man page is like a formal reference for a command. It usually lists the
command syntax, purpose, and descriptions of the command options. They ususally
do not include many examples, so use it more as a reference.

* `apropos <term>` - show appropriate commands based on search term
  * The first field shows the command man page, and the second field shows the
    section

## Module 4 - Piping and Redirecting I/O

### Redirecting Standard Output

To redirect standard output to a file instead of the terminal use the
redirection command:
* `>` - redirect output of a command to a file instead of a terminal
* Example: `ls -ltr ~/Documents > documents-output.txt`
* View the output of this command with `less documents-output.txt`

Note that using `>` will rewrite the destination file from the beginning. To
append to the file instead, use the `>>` command:
* `>>` - same as `>`, but appends file vs. rewriting file
* `echo "Hello" >> somefile.txt`
* `echo "Rutgers IEEE" >> somefile.txt`
* `less somefile.txt`

With this in mind, if we redirect nothing to a file (`> nothingfile.txt`), if
the file exists, it is truncated. If the file does not exist, it creates a new
empty file, similar to the command `touch nothingfile.txt`.

### Redirecting Standard Error

If we want to redirect standard error, we need to use the file descriptor
number. The three most common file descriptor numbers for I/O redirection are:
* 0 - standard input
* 1 - standard output (implied with `>` and `>>` commands)
* 2 - standard error

With this in mind, we can use `2>` or `2>>` to redirect standard error to a file
like how we did with standard output.
* `ls -t /bin/usr 2>> error-text.txt`

Sometimes we want to redirect both standard output and standard error to a file.
We can use `&>` or `&>>` to redirect both standard output and standard error.
* `ls -t /bin/usr &> error-std-text.txt`

One very useful thing we could do especially if we are using a command that puts
a lot of status and error messages to the terminal is directing it to a file
called `/dev/null` aka the *bit bucket*. This file accepts input but does
nothing with it. For example we could use this command with Okular (an awesome
PDF reader, but one that prints a lot of messages to the terminal).

`okular some-file.pdf &> /dev/null`

### Redirecting Standard Input

* `cat <file1> <file2> ... <fileN>` - reads files and copies input to standard
  output

For example, if you had a large file that was split into multiple parts (something
like `my-list.01.txt ... my-list.09.txt`, we could use `cat` to join the files
together:
 
`cat my-list.0*.txt > my-list.txt` 

### Pipelines

* `command 1 | command 2` - redirect standard output of command 1 to standard
  input of command 2`

A common example to do is view the the output of a command:

`ls /usr/local | less`

You can also pipe multiple commands together, for example:

`ls /usr/local /usr/bin | sort | less`

The first command lists the files and directories in `/usr/local` and `/usr/bin`
and then pipes it to the `sort` command. The `sort` command then sorts the input
list and outputs a sorted list of the files and directories. `less` than allows
the user to view the list.

`sort` is an example of a *filter*. Some other very useful filters are:
* `uniq` - omit repeated lines (use `uniq -d` to see the list of duplicated
  lines
* `wc` - display amount of lines, bytes, and words in a file (`wc -l` only will
  print the number of lines)
* `grep <pattern>` - display lines that match a pattern (simple text pattern or regular
  expression)
  * `-i` - ignore case
  * `-v` - print lines not matching pattern
* `head` - print first ten lines (can specify # of lines like `head -n 5`)
* `tail` - print last ten lines (can specify # of lines like `tail -n 3`)
* `tee <file>` - pipe output of command to both *file* and standard output

## Module 5 - Package Management Tools

On Linux systems, it's possible to install (most) of your software from the terminal. This is cool because it means no need to google around for everything, and there's an easy single way to update everything.

OS X has a package manager written for it called [homebrew](http://brew.sh/).
(Side note: check out [homebrew cask](http://caskroom.io/), which adds apps like Spotify to homebrew -- later! The internet in this room probably can't handle it.)

This section can't be done on the server, because it requires root access, so follow along locally or just sit tight.

### Searching
`$ apt-cache search latex`

### Installing
Once you know the name of the package you want to install, one command will install it for you. In this case we're installing the build tools (for compiling C and C++).
`$ sudo apt-get install build-essential`

Some commericial apps aren't available in the standard Ubuntu repositories, but you can find instructions for adding them online like for [Spotify](https://www.spotify.com/us/download/linux/).

### Upgrading
`$ sudo apt-get update`
`$ sudo apt-get upgrade`

## Module 6 - Compiling Programs from Source/Makefiles

Next we'll briefly touch on compiling C/C++ code. We're not getting into _writing_ C/C++ since that's a bit... involved.

Let's lay out a simple example. We have the file `main.c`:

```c
#include <stdio.h>

int main() {
    printf("ieee\n");
}
```

To compile it, `cd` into the directory where this file is, then enter `gcc main.c -o main`. `ls` to check that we've made a new file, `main`. Run it with `./main`.

But let's say you have a bigger project, across multiple files.

`main.c`:
```c
#include <stdio.h>
#include "helper.h"

int main() {
    printf(really_cool_string);
}
```

`helper.c`:
```c
char* really_cool_string = "ieee\n";
```

`helper.h`:
```c
char* really_cool_string;
```

Compile like before, but you need to compile both `main.c` and `helper.c`: `gcc main.c helper.c -o main`. If you leave out `helper.c` from the command it won't complain, but your program just won't work (thanks, C!).

Now imagine you have a bigger project, with twenty files. Typing out the compile command gets annoying, so... enter make files!

`make` is a tool to automate compiling. You write a file (name it `makefile`) with instructions on how to compile your project.

`makefile`:
```make
all:
    gcc main.c helper.c -o main

clean:
    rm main
```

If you run `make`, it'll do the first command, and if you run `make clean` it'll do the second (delete the binary).

But now, a cool trick: in big projects, compiling can take several minutes, so we want to avoid recompiling files that haven't changed.

```makefile
all: main.o helper.o
    gcc main.o helper.o -o main

main.o:
    gcc -c main.c

helper.o:
    gcc -c helper.c

clean:
    rm *.o main
```

We store intermediate compiled files as `.o` files, which we can quickly "link" together to finish the compile. If we change just `helper.c`, only `helper.o` would be recompiled, not `main.o`.


Rather than making make files yourself, though, you can find a sane [Generic Makefile](https://github.com/mbcrawfo/GenericMakefile) that'll compile and link all the source files in a directory.

## Module 7 - File Permissions

All files and directories in Linux have three main file attributes: read access,
write access, and execution access. If you do `ls -l` on some directory, you may
see something like this on the left side:

`-rwxrw-rw-`

The first character represents the file type. `-` represents a regular file. `d`
represents a directory. `l` represents a symbolic link (similar to a shortcut in
Windows).

The next triplets of `rwx` represent the actual permission attributes. The first
triplet represents permissions of the **owner**. The second triplet represents
permissions of the **owner's group** (groups are beyond the scope of this tutorial).
The last triplet represents permissions of the **world** (all other users). Our
example shows a regular file where the owner has read, write, and execution
access, while the owner's group and the world only has read and write access,
but no execution access.

We can change a file's permissions with the `chmod` command. Note that only the
owner or root can use this command.

There are two main ways to use the chmod command: octal digits or the symbolic
representation. 

`chmod 755 someScript.sh`

The 755 represents three octal digits each representing the permissions of the
owner, the owner's group, and the world respectively. For example, 7 in octal
represents the binary number 111 -> `rwx`. 5 in octal represents the binary
number `101` -> `r-x`. So the above command will set `someScript.sh` to have
read, write, and execution access for the owner, and read and execution access
for the owner's group and the world.

In symbolic notation, there are a few symbols to note:
* `u` - user (file/directory owner)
* `g` - group owner
* `o` - others (world)
* `a` - all (implied if not specified)

We then add a few more symbols:
* `+` - add permission
* `-` - remove permission
* `=` - set permission

With both of these, we now can write some example settings:
* `u+x` - add execution access to the owner
* `o-rw` - remove read and write permissions from world
* `u-x, o=rw` - remove execution access from owner, set world to have read and
  write access

## Module 8 - References

www.linuxcommand.org

www.ee.surrey.ac.uk/Teaching/Unix
