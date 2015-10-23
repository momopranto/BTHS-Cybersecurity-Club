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

* #### Some characters and their functions:
  - will be updated soon

* :)

## Web Tools
will be updated soon :))

## FTP and SCP
will be updated soon :)))

## ```apt-get``` and ```apt-cache```
will be updated soon :))))

[1]:https://www.gnu.org/software/emacs/
[2]:http://www.vim.org/
[3]:http://openvim.com/
[4]:http://www.codecoffee.com/tipsforlinux/articles/25.html
[5]:https://www.digitalocean.com/community/tutorials/what-is-ftp-and-how-is-it-used
[6]:https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection



