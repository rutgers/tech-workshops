# Rutgers IEEE Student Branch - Python Basics Workshop

## Workshop Leaders

Ravi Bhankharia, Niral Shah

## Module 0 - Initial Download and Setup

We'll be using Python 3.5.0 for this tutorial, get them at the links below:

For Windows: https://www.python.org/downloads/windows/

After you download it, double click on the package and click through the Python 3 installer. Make sure you check the system path option.

## Module 1 - Pip and Virtual Environments

### A. Pip

Python makes it simple to get new libraries using a tool called pip. With Python 3 it comes with the download. Use it just by typing this into terminal (replace library-name with the actual library):

** `pip install library-name`

### B. Virtual Environments 

When working on a specialized project, you may not want to install your libraries globally on your machine in case an update to a library breaks the previous code you were working on. Virtual environments fix this problem by creating a directory that is separate from your normal python installation where you can install any number of libraries that are unique to that folder. To install virtualenv, type in:

** `pip install virtualenv`

After installing virtualenv, navigate to the directory where you want to create your virtual environment and type:

** `virtualenv env`

where env is the name of your virtual environment. After running this command you'll see a new directory pop up with the name of your environment. To work in your virtual environment use the following command:

** `cd env/Scripts`

** `activate`

This will make it so that any time you type `pip install library-name` it will only be installed in your environment. To get out of the environment, merely type `deactivate`.

### C. requests and beautifulsoup4

For the webscraping tutorial, we'll be using two libraries - requests and Beautiful Soup 4. Activate your virtual environments and type in:

** `pip install requests beautifulsoup4`


## Module - References
http://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/
