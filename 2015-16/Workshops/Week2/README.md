#Week 2: Virtual Machines and Linux

You can find this week's presentation [here](https://docs.google.com/presentation/d/15B-QUuf6CjwKjWJIWiXk46wcXsKYmvMeDM2hWBdriWk/edit?pli=1#slide=id.gcb84b61d4_0_116).

###Desktop vs. Server
* Desktop
  - User friendly (GUI, see below)
  - Comes with applications and software that you do need, along with additional software that is not crucial to your machine's function (iMovie on Mac, for example)
  - Can be used for any purpose
  - Portability
  - Modularity
* Server
  - Always on
  - Accessibly over the internet or a private network
  - No GUI
  - comes with ONLY the software that you need for BASIC functionality
  - usually configured for a specific purpose

###Linux vs. Windows Servers
Linux acts a much more convinient service; while windows servers require restarts for updates and to modify programs (installing/uninstalling), Linux rarely requires restarts.  Linux also offers greater stability and security, and is free!

###Virtual Machines
* Flexibility 
  - Are hosted on remote servers and run in a window on your screen
  - Allow you to experiment with different operating systems.
* Safety
  - Great for cyber security excercises, act like insurance; if you get a virus on a VM, it's not problem since it doesn't affect your actual computer.
* Cross OS interaction
  - Allow you to use software only available on certain operating systems.

###LUI vs. GUI: User Interfaces
A user interface is where humans and machines interact.
* GUI - Graphical User Interface
  - The software you use on a daily basis is a GUI.  When you interact with your computer's desktop, you click buttons to launch applications.  A GUI is visual, and is generally easier to understand than a LUI. 
* LUI - Line User Interface
  - Also known as a CLI, a command user interface, this user interface allows users to communicate with the machine through text.  Using your linux terminal or windows command prompt and using the commands listed below, you can launch applications, view and modify files, and more.

### The Command Line
Two different types- one of those internal rivalry debate things amongst programmers
* Bash - **B**ourne **A**gain **SH**ell
  - Most commonly supported
  - Scripting support, closely follows POSIX standards
* Z Shell (zsh)
  - Less common
  - Better tab completion, command corrections, less strict with POSIX

###Basic Linux Terminal Commands
* ```man``` - displays "manual", can be used with any other command to display definition/function
* ```mkdir``` - creates a directory
* ```ls``` - lists all the files ```(-a/l/r)```
* ```cd``` - change working directory
* ```pwd``` - print working directory
* ```mkdir``` - create a directory
* ```cp``` - copy a file or directory ```(-R)```
* ```mv``` - move a file or directory ``` (-R)```
* ```rm``` - delete a file or directory ```(-R/f)```
* ```clear``` - clears your terminal window of past commands

##### Wildcard Operator
The ```*``` operator can be used in many ways:
* ```<command> foo/*``` affects all files in directory foo
* ```<command> *.txt``` affects all files with names ending in “.txt”
* ```<command> img*``` affects all files with names starting with “img”
* ```<command> *k*``` affects all files with names containing “k”

### Sudo and Root
sudo make me a sandwich
<br />
* Root is the highest level user in a unix/linux system
* Most OS’s do not allow users to login as root but can execute operations as root temporarily using “sudo”
* Some files and programs can only be accessed by root
* You can call any command as root by adding ```sudo``` to the beginning of the command:
  - ```sudo rm```, for example

