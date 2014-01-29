import re
import sys
sys.path.insert(0, '../')
import regex
import tokens

state = 1
lexeme = ""
data = None
     
# State 1 - default
# State 2 - just read a letter or a digit, if _ go to state 3
# State 3 - just read an _, must break if next read is _, if letter/digit return to state 2
# State 4 - accept state, there is no more characters in line and the last state was 2
def AlphaFSA(line):
   data = line
   token = null
   states = {
       1: stateOne,
       2: stateTwo,
       3: stateThree
   }

   while (state != 4):
       if data.__len__() < 1 and state == 2:
           state = 4
       else:
           states[state]

   if tokens.reservedWords[lexeme]:
       token = [tokens.reservedWords[lexeme], lexeme]
   else:
       token = ["MP_IDENTIFIER", lexeme]

   return token


def stateOne():
   current = data[0]
   if re.match(regex.letter, current):
       state = 2
       lexeme += current
       data = data[1:]
   elif re.match('_', current):
       state = 3
       lexeme += current
       data = data[1:]
   else:
       #Handle error code...
       print "Scan Error Found in State One"

def stateTwo():
   current = data[0]
   if re.match(regex.letter, current) or re.match(regex.digit, current):
       state = 2
       lexeme += current
       data = data[1:]
   elif re.match('_', current):
       state = 3
       lexeme += current
       data = data[1:]
   else:
       state = 4

def stateThree():
   if re.match(regex.letter, current) or re.match(regex.digit, current):
       state = 2
       lexeme += current
       data = data[1:]
   else:
       #Handle error code...
       print "Scan Error Found in State Three"
