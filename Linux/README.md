# Rutgers IEEE Student Branch - Linux Workshop

## Workshop Leaders

Sam Lotsvin, Revan Sopher, Jeremy Savarin

## Module 0 - Linux Installation

More to come.

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

* `cd <dir>` - change current working directory to *<dir>*

For this section, here is some useful notation to know:
* `/` - the root directory
* `~` - the home directory
* `.` - the current directory
* `..` - the parent directory

You don't have to be in a certain directory to list the directory's contents. You can list any directory's contents with:
* `ls <dir>` - list files in directories of *<dir>*

You can also get information about any file you encounter. Use the following commands:
* `file <file>` - get information about *<file>*'s type
* `less </path/to/file>` - view contents of a file

Play around, and remember! If you ever get lost, remember these key shortcuts!
* `cd` - (no arguments) return to home directory
* `cd -` - return to previous directory
* `cd ..` - return to parent directory

## Module 2 - File/Directory Manipulation

More to come.

## Module 3 - Command Information and Manpages

More to come.

## Module 4 - Piping and Redirecting I/O

More to come.

## Module 5 - Package Management Tools

More to come.

## Module 6 - Compiling Programs from Source/Makefiles

More to come.

## Module 7 - Putting it All Together

More to come.

## Module 8 - References

More to come.
