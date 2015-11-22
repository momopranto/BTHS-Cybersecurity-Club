# Becoming One With Linux

The presentation from this week's workshop is available [here](https://goo.gl/H3Z5jp).  If you don't understand the memes, read up!

## Job Control
Practical shortcuts within the linux terminal:
* ```Ctrl+c``` - kill a job in the foreground (quit/cancel)
* ```Ctrl+z``` - suspend a job (stop)
* ```Ctrl+d``` - terminate a job
* ```fg``` - resume a job in the foreground
* ```bg``` - resume a job in the background
* ```kill``` - kill a job (background or foreground)
* ```jobs/top``` - list ongoing jobs or processes

## Vim
* better than [emacs][1]
* download: ```sudo apt-get install vim```
* **this [tutorial link][3] is the only way you will learn all the shortcuts- just staring at a reference list won't help you!**

* #### Modes
  - normal
  - insert (this one is for editing)
    - ```esc``` to exit insert mode
  
* #### Commands
Execute vim commands from normal mode by typing ```:``` and then the command.
  - ```q``` - quit
  - ```w``` - write
  - ```!``` - force

* #### Keyboard Commands
check out that tutorial link now and walk through all of these!
  - ```w``` - go to start of next word
  - ```e``` - go to end of current word
  - ```b``` - go to beginning of current word
  - ```v``` - select text
  - ```y``` - copy (yank) selected text
  - ```d``` - cut (also used to delete) selected text
  - ```p``` - paste

* #### advAnCeD vim
It's about to get faster and more efficient up in here:
  - ```yy``` - *copy* an entire line
  - ```dd``` - *cut* an entire line
  - ```ni<text>``` - inserts ```<text>``` n times 
  - ```nf<letter>``` - find *n*th letter 
  - ```*``` - find next occurrence of current word
  - ```#``` - find previous occurrence of current word
  - ```nG``` - goto line *n*
  - ```/<text>``` - search for ```<text>``` (n for next occurrence)

## Text Programs
These are more vim commands you can use in the terminal; they're useful for when you're modifying or viewing text files/programs.

* ```cat``` - prints out contents of a file
* ```echo``` - prints text to the console
* ```less``` - lets you view and scroll through a file
* ```grep``` - insanely useful pattern matcher
  - think of ```grep``` as the ```Ctrl+F``` of the terminal, but for your whole computer
    - search for a word in text files or file names
    - supports regular expressions
    - very useful in combination with [pipe][4] ```|```

## Standard Input/Output (stdio)
The idea of this is pretty straight forward: programs take input from the console (the keyboard) and print its output on the console (the screen).

#### Some characters and their functions: (input)
  - ```>``` - Redirects standard output
  - ```>&``` - Redirects standard output and standard error
  - ```<``` - Redirects standard output
  - ```|``` - Pipe; redirects standard output to another command
  - ```>>``` - Append (add on to) standard output
  - ```>>&``` Append standard output and standard error

## Web Tools
These are commands that allow you to connect to and modify files from the web.

* ```wget``` - download a file from web
* ```curl``` - data transfer tool that can be used to make http requests (GET/POST)
  - GET/POST affects how data is encrypted in a websites URL
* ```nc``` - open or connect to a TCP/UDP websocket
  - TCP/UDP are two encryption protocols that protect data packets as they are sent across the web
* ```ssh``` - remotely connect to another computer

## FTP and SCP
* **FTP**: **F**ile **T**ransfer **P**rotocol
  - FTP is used to transfer files from one host to another.  An example of this is using an FTP client to update a website; the client would transfer files hosted on your computer locally to a remote server where they can be accessed anywhere online.
  - Terminal Commands:
    * ```connect``` - connect to a remote FTP server
    * ```!<command>``` - excecute as local server
    * ```get``` - download file from remote directory
    * ```put``` - upload file to remote directory
    * Other commands we've covered, like ```ls```, ```cd```, ```mkdir```, etc, also apply.

## ```apt-get``` and ```apt-cache```
* commands used to download and work with software packages, and is tied into the Debian package manager.
* allow you to manage things you download
* Commands:
  - ```upgrade``` - install newest version of all packages
  - ```update``` - resync packages indexes; update
  - ```install``` - install package (program)
  - ```remove``` - uninstall package
  - ```apt-cache-search``` - search package in indexes

#Yus
You are now ready to attempt the excercise! 

[1]:https://www.gnu.org/software/emacs/
[2]:http://www.vim.org/
[3]:http://openvim.com/
[4]:http://www.codecoffee.com/tipsforlinux/articles/25.html
[5]:https://www.digitalocean.com/community/tutorials/what-is-ftp-and-how-is-it-used
[6]:https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection



