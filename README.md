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

## Example Output
This is the output when the file is run on utf16-le.txt  

    00000000  74 00 68 00 69 00 73 00  20 00 69 00 73 00 20 00  |t.h.i.s. .i.s. .|  
    00000010  61 00 20 00 74 00 65 00  73 00 74 00 20 00 66 00  |a. .t.e.s.t. .f.|  
    00000020  69 00 6c 00 65 00 0a 00  74 00 68 00 69 00 73 00  |i.l.e...t.h.i.s.|  
    00000030  20 00 69 00 73 00 20 00  61 00 6e 00 6f 00 74 00  | .i.s. .a.n.o.t.|  
    00000040  68 00 65 00 72 00 20 00  6c 00 69 00 6e 00 65 00  |h.e.r. .l.i.n.e.|  
    00000050  0a 00                                             |..|  
