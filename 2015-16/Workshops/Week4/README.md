# File Forensics

This week's presentation is available [here](https://goo.gl/rwUSWy).

### What do we know about files?

Different types of files have different file extensions such as .mp3 or .jpg.
That helps us understand what kind of file it is and what we need to open it with.

### But how does the computer tell the difference?
All files have raw binary data that looks something like this:
![](http://tierradatarecovery.co.uk/wp-content/uploads/2013/05/pic1.jpg)

This raw data can be viewed in a hex editor such as [XVI32](http://www.chmaas.handshake.de/delphi/freeware/xvi32/xvi32.htm) or [frhed](http://frhed.sourceforge.net/en/) for Windows. Linux/Unix has a built in hex editor called ```xxd```

  
### File Signatures

Every type of file has its own unique file signature that helps the computer identify it. Every file has an opening and a closing called a header and a footer, respectively.

This is similar to how in HTML there are opening and closing tags like this:

<html>

    <head>
        some stuff
    </head>
    <body>
        some stuff
    </body>

</html>

[Here](http://www.garykessler.net/library/file_sigs.html) is a great resource where you can find the file signatures for most common files.

For example the header for a jpg file is: ```FF D8 FF E0```

And the footer (end of the file) would be: ```FF D9```


### Catfish Files
*(not actually what they're called)*


![Catfish](http://mtvasia-com.mtvnimages.com/mtvasia-shows/catfish-meaning.jpg)

In this case, files can pretend to be something they're not. Changing a file extension does NOT change any of the hex data. A jpg does not become an mp3 just because you change the extension in the name.

You can verify the files true format by checking its signature or running the linux/unix `file` command.

### File Carving

Data can be extracted or recovered from a file by using the ```dd``` command.

Usage: `dd if=input_file of=output_file bs=? count=? skip=?`

- bs=(number of bytes at a time) 
- count=(number of times you want to copy the bs) 
- skip=(where you want to start copying from)

Count and skip are optional parameters. Leaving count blank will just copy the entire input file. Leaving skip blank will just start copying from the beginning of the file.

Another great resource [here](http://dirtbags.net/ctf/tutorial/carving.html)

### LSB Steganography

[Steganography](http://www.garykessler.net/library/steganography.html) is the science of hiding data, usually in plain sight.
  
Data can be hidden in images by storing the information in the least significant bits of a pixel.
![](https://www.ethicalhacker.net/i/features/books/terrornet/terror4.jpg)

One pixel can represent a **LOT** of different colors through some combination of red, green, and blue. The above picture tells us the amount of red, green, and blue in the pixel in binary. We can also put this in normal rgb notation as rgb(44,44,44) but to understand how the data is hidden we need to look at it in binary.

Lets say we have a word we want to hide like: "hello".
We can convert this to its binary equivalent as
```01101000 01100101 01101100 01101100 01101111```

Next, we take the first 2 bits of the 'h' and replace them in the last 2 bits of the red byte of the pixel above.

<code>001011<b>00</b></code> -> <code>001011<b>01</b></code>

This is repeated for the blue and green bytes of the pixel. Then we continue this process with the next pixel and repeat until we have have inserted all bytes of hello.

### Steg Tools

  - MS Paint: the basics are great
  - GIMP: Free open source photoshop
  - Stegsolve: image analyzer, solver and data extractor
  - Steghide: extract hidden data (involves passphrases)
  - Python PIL: Python library for working with images
  
### Other Forensics Tools

  - Strings: linux command to parse strings in a file
  - File: linux command to identify a file type
  - Exiftool: linux tool to read, write, and manipulate metadata
  - Scalpel/Foremost: file carving program


  
