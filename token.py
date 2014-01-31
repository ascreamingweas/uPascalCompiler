class ScanError(Exception): pass

class Token:
    """
    A Token object contains {type, lexeme, line#, col#}
    """

    def __init__(self, startChar):
        self.lexeme = startChar.lexeme
        self.sourceText = startChar.sourceText
        self.lineIndex = startChar.lineIndex
        self.colIndex = startChar.colIndex
        self.type = None


    def show(self):
        tokenTypeLen = 0
        space = " "
        s = ""
        # Used for printing out the token
        if self.type == self.lexeme: 
            s = s + "Symbol" + ":" + space + self.type
        elif self.type == "Whitespace": 
            s = s + "Whitespace" + ":" + space + repr(self.lexeme)
        else:
            s = s + self.type + ":" + space + self.lexeme
        return s
             
    # guts = property(show) #Not sure what this is

    def abort(self,msg):
        lines = self.sourceText.split("\n")
        sourceLine = lines[self.lineIndex]
        raise ScanError("\nIn line " + str(self.lineIndex + 1)
               + " near column " + str(self.colIndex + 1) + ":\n\n"
               + sourceLine.replace("\t"," ") + "\n"
               + " "* self.colIndex
               + "^\n\n"
               + msg)


    def getType(self):
        return self.type

    def getLexme(self):
        return self.lexeme

    def getLineNumber(self):
        return self.lineIndex

    def getColNumber(self):
        return self.colIndex
