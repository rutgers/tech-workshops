# Rutgers IEEE Student Branch - Linux Workshop

## Workshop Leaders

Sam Lotsvin, Revan Sopher, Jeremy Savarin

## Module 0 - Linux Installation

More to come.

## Module 1 - Navigating the File System

### 1a. Starting Out

When you first open your terminal, most likely you will see the following:

```shell
[jeremy@UnsungWitness ~]$
```

The first item is your **username**. The second item is your computer's **hostname**.
See the `~` symbol? That's shorthand for your **home directory**. The `$` symbol
will be explained in a later module. But for now, know that when you first open
a terminal, you will most likely start out in the home directory. Of course, our
journey should start close to home right?

Our home directory (and all subdirectories) is the only place where regular
users can write files. Elsewhere, we would need root privileges to write a file
(which will be explained in a later module).

If we want to know our current directory, we can use the following command:
* `pwd` - print working directory

For example, if I opened a terminal and entered `pwd`, I would get the following
output:

``` shell
/home/jeremy
```
So what's in this directory? We can use the following command to find out: 
* `ls` - list files and directories in current working directory

In the home directory, you will most likely have a number of directories
(Documents, Downloads, Pictures, etc.). We can actually see what is in these
directories without entering them. Use the following command:
* `ls *dir*` - list files and directories in *dir*

Now we can figure out what the contents of other directories are. But how do we
get to them? We need to change directories with the following command:
* '`cd *dir*` -  change working directory to *dir*

To better understand navigation, let's take a look at the Linux filesystem. It's
much like a tree. The filesystem begins at the root directory `/` and all other
directories branch from this root. 
More info about absolute vs. relative paths...

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
