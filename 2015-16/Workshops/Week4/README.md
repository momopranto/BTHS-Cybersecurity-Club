# File Forensics

This week's presentation is available [here](https://goo.gl/rwUSWy).

## What is a file?

* Different file extensions hold different kinds of data.
* What makes one file different from another file?
* How does the computer tell the difference?

### Raw Data

  Data collected from the source that has not been processed for use.
  
### File Signatures

  - Hex editors: XVI32, Frhed (windows), xxd, hd (Unix/Linux)

### Catfish Files

  Catfish: To pretend to be someone you're not by posting false information.
  * Changing a file extension does NOT change any of the hex data
  * A jpg does not become an mp3 just because you change the extension in the name.
  * You can verify the files true format by checking its signature.

### File Carving

  - Recovering files or fragments of files by analyzing raw data
  - Data can be copied bit by bit using an incredibly powerful(and dangerous) tool called “dd” (also known as direct copy)
  - dd if = input.file of=output.file 
  - bs = block size 
  - count = number of blocks
  - skip = offset to start copying

## Steganography

  The science of hiding data, usually in plain sight.
  
### LSB Steganography

LSB: Hiding messages in the least significant bytes of some data.

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


  
