# this-is-an-exe.exe

Solution:
When you have an exe file that says, “This is an exe” it comes off as pretty suspicious. So why not check to see if it is REALLY an exe file; and that’s what I did.

1. First, in order to see the raw data you will need a hex editor. Since I was using windows for this, I downloaded XVI32 (For Linux Users, you guys have a built in hex editor already: xxd).

2. Next, of course, I downloaded the exe file and, using XVI32, I opened it.


3. When I opened it I saw this:
	
	![](images/initial.png?raw=true)

4. Now that I see the raw data, in order to find out what the file really is, you need to obtain its File Signature. In order to find that, you look for its header and footer.
For this file, it is:
	Header:
	
	![](images/header.png?raw=true)

	Footer:
	
	![](images/footer.png?raw=true)
 

5. Now that you have the header and footer of the file, you go to www.garykessler.net/library/file_sigs.html (Resource for File Signatures) and find it.

6. I used control find and input the header into the search bar and it brought me to this:
	
	![](images/final.png?raw=true)
 	
	I guess that file was not an exe, but rather a png file.

7. Also, if it helps, It literally says “%PNG”
	
	![](images/png.png?raw=true)


