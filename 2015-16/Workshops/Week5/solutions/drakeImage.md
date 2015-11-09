### Solution to drake.jpg

1. Log on to your butterfly server account.

2. Open the drake.jpg image on github and click raw.

3. Download the the file using ```wget```:

   `wget urlOfImage`
  
4. Look at the file signature using ```xxd```:

   `xxd drake.jpg`
   
5. Use ```grep``` to find a pattern:

   `xxd drake.jpg | grep 'PK'`
   
6. Carve the file:
 
   `dd if=drake.jpg of=newFileName.zip bs=? count=? skip=?`

7. Unzip the file:

   `unzip newFileName.zip`

8. Upload the file and follow the link using ```imgur```.

   `imgur congration.jpg`
   
YAY PROBLEM SOLVED!


