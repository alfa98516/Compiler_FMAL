import sys
import re
from LToken import LToken
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
        self.curr_char = ""
        self.semicolFlag = False
        
    def get_next_token(self):
        curr_token = LToken("", LToken.END)
        curr = ""
        lexeme = ""
        while 1:
            if self.curr_char:
                curr = self.curr_char
                print("assignment of curr")
                self.curr_char = ""
            else:
                curr = sys.stdin.read(1)
            
            
            if not lexeme: # check if anything is in lexeme, if theres nothing, were not throwing a potential token away.
                if curr == self.ASSIGN:
                    curr_token.token_code = curr_token.ASSIGN
                    curr_token.lexeme = self.ASSIGN
                    return curr_token
            
                if curr == self.SEMICOL:
                    curr_token.token_code = curr_token.SEMICOL
                    curr_token.lexeme = self.SEMICOL

                if curr == self.PLUS:
                    curr_token.token_code = curr_token.PLUS
                    curr_token.lexeme = self.PLUS
            
                if curr == self.MINUS:
                    curr_token.token_code = curr_token.MINUS
                    curr_token.lexeme = self.MINUS
            
                if curr == self.MULT:
                    curr_token.token_code = curr_token.MULT
                    curr_token.lexeme = self.MULT
            
                if curr == self.LPAREN:
                    curr_token.token_code = curr_token.LPAREN
                    curr_token.lexeme = self.LPAREN

                if curr == self.RPAREN:
                    curr_token.token_code = curr_token.RPAREN
                    curr_token.lexeme = self.RPAREN
                
                if curr_token.lexeme:
                    return curr_token
            
            if curr == " " or curr == self.ASSIGN or curr == self.SEMICOL or curr == self.PLUS or curr == self.MINUS or curr == self.MULT or curr == self.LPAREN or curr == self.RPAREN:
            
                self.curr_char = curr if curr != " " else ""
                
                curr_token.lexeme = lexeme.strip()
                self._assign_code(curr_token)
                
                return curr_token

            lexeme += curr
    
    def _assign_code(self, token):
        IDMatch = self.ID.match(token.lexeme)
        INTMatch = self.INT.match(token.lexeme)
        

        if token.lexeme == self.PRINT:
            token.token_code = token.PRINT
        
        elif token.lexeme == self.END:
            token.token_code = token.END
        
        elif IDMatch is not None and token.lexeme == IDMatch.group():
            token.token_code = token.ID

        elif INTMatch is not None and token.lexeme == INTMatch.group():
            token.token_code = token.INT

        else:
            token.token_code = token.ERROR

