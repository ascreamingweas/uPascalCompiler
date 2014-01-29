import token
import alpha

"""
This is the scanner portion of our microPascal compiler
"""

#Scan things
class Scanner():
 
    def openFile(fname):
        f = open(fname, 'r')
        return f

    def getTokens(fileObject):
        for line in fileObject:
            getNextToken(fileObject[line])
 
    def getNextToken(line):
        foundToken = None
 
        if re.match(regex.alpha, line[0]):
            print "Found Alpha: " + line[0]
            foundToken = alpha.AlphaFSA(line)
 
 
    def __init__(self):
        self.token = token.Token()
