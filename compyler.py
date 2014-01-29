import scanner
import sys

"""
microPascal compiler implemented in Python

This is the main driver for the program
"""

def main():
    print "We have started the compiler"
    fname = sys.argv[1]
    Scanner = scanner.Scanner()
    newfile = Scanner.openFile(fname)
    lines = newfile.readlines()
    Scanner.dispatcher(lines)


if __name__ == "__main__":
    """Main"""
    start()
