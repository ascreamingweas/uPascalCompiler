##FSA plugin with all implemented FSA methods
from token import *
from tokens import *
from tokenTypes import *
import scanner as scanner

class ScanError(Exception): pass

"""FSA for Whitespace and Comments"""
def process_whitespace():
    while char1 in WHITESPACE_CHARS:
        token = Token(character)
        token.Type = types.MP_WHITESPACE
        getChar() 

        while char1 in WHITESPACE_CHARS:
            token.lexeme += char1
            getChar()

    # process comments
    while char2 == "/*":
        # comment start
        token = Token(character)
        token.Type = types.MP_COMMENT
        token.lexeme = char2

        getChar()
        getChar()

        while not (char2 == "*/"):
            if char1 == types.MP_EOF:
                token.abort("Found end of file before end of comment")
            token.lexeme += char1
            getChar()

        token.lexeme += char2 # append the */ to the token lexeme

        getChar()
        getChar()

def identifier_fsa(token):
    token.Type = types.MP_IDENTIFIER
    getChar() 

    while char1 in IDENTIFIER_CHARS:
        token.lexeme += char1
        getChar() 

    if token.lexeme in ReservedWords: token.Type = ReservedWords[token.lexeme]
    return token

def numbers_fsa(token):
    token.Type = types.MP_INTEGER_LIT
    getChar()

    while char1 in INTEGER:
        token.lexeme += char1
        getChar()

    if char1 == ".":
        token.lexeme += char1
        token.Type = types.MP_FIXED_LIT
        getChar()
        while char1 in INTEGER:
            token.lexeme += char1
            getChar()

    if char1 in ["E", "e"]:
        token.lexeme += char1
        getChar()
        token.lexeme += char1
        token.Type = types.MP_FLOAT_LIT
        getChar()
        while char1 in INTEGER:
            token.lexeme += char1
            getChar()

    return token

def string_fsa(token):
    # Save type of quote (' or ") so we can match
    quoteChar = char1
    getChar() 

    while char1 != quoteChar:
        if char1 == types.MP_EOF:
            token.abort("Found end of file before end of string literal")

        token.lexeme += char1
        getChar()

    token.lexeme += char1
    getChar()         
    token.Type = types.MP_STRING_LIT
    return token

def symbols_fsa(token):
    token.Type = SingleCharacterSymbols[token.lexeme]
    getChar()
    if char1 in ["=", ">"]:
        token.lexeme += char1
        token.Type = SingleCharacterSymbols[token.lexeme]
        getChar()

    return token

#------------------------------------
def getChar():
    global char1, char2, character
    character = scanner.getNextChar()
    char1 = character.lexeme
    # Always get next char (2 ahead)
    char2 = char1 + scanner.lookahead(1)