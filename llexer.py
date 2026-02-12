import sys
import re
from ltoken import LToken
class LLexer:
    ID = re.compile('[A-Za-z]+')
    INT = re.compile('[0-9]+')
    ASSIGN = '='
    SEMICOL = ';'
    PLUS = '+'
    MINUS = '-'
    MULT = '*'
    PRINT = 'print'
    END = 'end'
    LPAREN = "("
    RPAREN = ")"
    def __init__(self):
        self.last = ""
    
    def get_next_token(self):
        curr_token = LToken("", LToken.END)
        curr = ""
        lexeme = ""
        while 1:
            if not self.last:
                curr = sys.stdin.read(1)
            else:
                curr = self.last
                self.last = ""
        
            if curr.isspace():
                curr = sys.stdin.read(1)

            lexeme+=curr

            if curr.isdigit():
                curr = sys.stdin.read(1)
                while curr.isdigit():
                    lexeme+=curr
                    curr = sys.stdin.read(1)
                self.last = curr
                curr_token.lexeme = lexeme.strip()
                curr_token.token_code = curr_token.INT
                return curr_token
            
            elif curr.isalpha():
                curr = sys.stdin.read(1)

                while curr.isalpha():
                    lexeme+=curr 
                    curr = sys.stdin.read(1)
                self.last = curr

                if lexeme.strip() == "print":
                    curr_token.token_code = curr_token.PRINT
                    curr_token.lexeme = "print"
                elif lexeme.strip() == "end":
                    curr_token.token_code = curr_token.END
                    curr_token.lexeme = "end"
                else:
                    curr_token.token_code = curr_token.ID
                    curr_token.lexeme = lexeme.strip()
                
                return curr_token
            
            else:
                curr_token.lexeme = curr
                self._assign(curr_token)
                return curr_token
    

    def _assign(self, token):
        if token:
            if token.lexeme == "+":
                token.token_code = token.PLUS
                return token
            
            elif token.lexeme == "-":
                token.token_code = token.MINUS
                return token

            elif token.lexeme == "=":
                token.token_code = token.ASSIGN
                return token
            
            elif token.lexeme == "*":
                token.token_code = token.MULT
                return token
            
            elif token.lexeme == ";":
                token.token_code = token.SEMICOL
                return token

            elif token.lexeme == "(":
                token.token_code = token.LPAREN
                return token
            
            elif token.lexeme == ")":
                token.token_code = token.RPAREN
                return token

        token.token_code = token.ERROR
        return token

