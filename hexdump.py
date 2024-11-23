# Ashton Johnson, CS543, Assignment 1
#
# This program imitates a 'clean room' version of hexdump
# It takes in a file and prints out a table that shows the byte numbers,
# the bytes in hex, and the inspection mode output
#
# It's run using "python hexdump.py {filename}"

import argparse


def main():
    # Setting up the program to take in a file
    parser = argparse.ArgumentParser(description="Runs a 'clean room' version of Hexdump on the given file")
    parser.add_argument("file", help="File to be parsed")
    args = parser.parse_args()

    # Assure file was parsed
    if args.file:
        # Variable tracks the line number for column 1
        linenum = 0
        # Read in as binary
        with open(args.file, 'rb') as readFile:
            # Assure that the file contains something. If not, print out "00000000" as hexdump would
            word = readFile.read(16)
            if len(word) == 0:
                print("00000000")
            # While there is stuff in "word"
            while 1:
                # Exit statement
                if len(word) == 0:
                    break

                # Building the inspection mode data for column 3
                inspection = str("|")
                for i in word:
                    if 128 > i > 31:
                        inspection += chr(i)
                    else:
                        inspection += "."
                inspection += "|"

                # Building/formatting the data for column 2
                line = '{:08x}'.format(linenum) + "  "
                line = line + " ".join("{:02x}".format(i) for i in word[:8])
                line = line + "  "
                line = line + " ".join("{:02x}".format(i) for i in word[8:])

                # Checking to see if the last line contains a full 16 bytes or not for formatting purposes
                if len(word) % 16 == 0:
                    line += "  " + inspection
                elif len(word) > 8:
                    line += " " * (3 * (16 - len(word)) + 2) + inspection
                elif len(word) <= 8:
                    line += " " * (3 * (16 - len(word)) + 1) + inspection

                # Printing one line of 16 bytes
                print(line)
                # Prepping for next run of while loop
                linenum = linenum + 16
                word = readFile.read(16)


if __name__ == '__main__':
    main()
