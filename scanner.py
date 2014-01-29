import token
import alpha

"""
This is the scanner portion of our microPascal compiler
"""

#Scan things
class Scanner():
    colNum = None
    lineNum = None
    token = None
    lexeme = None
 
    def openFile(fname):
        f = open(fname, 'r')
        return f

    def getLexeme():
        return lexeme
 
    def getLineNumber():
        return lineNum
 
    def getColumnNumber():
        return colNum

    def dispatcher(file):
        for line in file:
            getNextToken(file[line])
 
    def getNextToken(line):
        foundToken = None
        if re.match(regex.alpha, line[0]):
            print "Found Alpha: " + line[0]
            foundToken = alpha.AlphaFSA(line)
