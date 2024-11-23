# clean-hexdump
This program imitates a 'clean room' version of hexdump  
It takes in a file and prints out a table that shows the byte numbers, the bytes in hex, and the inspection mode output.  

## Files
hexdump.py contains the code for the project  
d.txt is a test file in utf-8 encoding  
utf16-le.txt is a test file in utf16 little endian encoding  
The other files - empty, exact, long, longer, and short - are all different test cases for the display of the inspection mode output.  

## Running
> python hexdump.py {filename}  
