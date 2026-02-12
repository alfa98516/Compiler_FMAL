import sys
from llexer import LLexer
from ltoken import LToken


# Statements -> Statement ; Statements | end
# Statement -> id = Expr | print id
# Expr- > Term | Term + Expr | Term – Expr
# Term -> Factor | Factor * Term
# Factor -> int | id | ( Expr ) 


class LParser:
    def __init__(self, lexer):
        self.LLexer = lexer
        self.LToken = None

    def parse(self):
        self.next_token()
        self.statements()
        print()

    def error(self):
        print("Syntax error")
        quit()

    def next_token(self):
        token = self.LLexer.get_next_token()
        if token.token_code == token.ERROR:
            self.error()
        self.LToken = token

    def statements(self):

        if self.LToken.token_code == self.LToken.END:
            return
        
        self.statement()

        if (self.LToken.lexeme != self.LLexer.SEMICOL):
            self.error()

        self.next_token()
        self.statements() 
    
    def statement(self):
        
        if self.LToken.token_code == self.LToken.PRINT:
            self.next_token()
            if self.LToken.token_code != self.LToken.ID:
                self.error()
            
            print(f"PUSH {self.LToken.lexeme}")
            print("PRINT")
            self.next_token()
            return
        
        if self.LToken.token_code == self.LToken.ID:
            print(f"PUSH {self.LToken.lexeme}")
            self.next_token()

            if self.LToken.token_code != self.LToken.ASSIGN:
                self.error()

            self.next_token()
            self.expression()
            print("ASSIGN")
            return

        else:
            self.error()

            
    def expression(self):
        self.term()

        if self.LToken.token_code == self.LToken.SEMICOL:
            return

        elif self.LToken.token_code == self.LToken.PLUS:
            self.next_token()
            self.expression()
            

            print("ADD")
            return
        
        elif self.LToken.token_code == self.LToken.MINUS:
            self.next_token()
            self.expression()
            print("SUB")
            return
    
    def term(self):
        self.factor()
        self.next_token()
        if self.LToken.token_code != self.LToken.MULT:
            return
        
        else:
            self.next_token()
            self.term()
            print("MULT")
    

    def factor(self):
        if self.LToken.token_code == self.LToken.ID or self.LToken.token_code == self.LToken.INT:  
            print(f"PUSH {self.LToken.lexeme}")
            return
        
        if self.LToken.token_code == self.LToken.LPAREN:
            self.next_token()
            self.expression()

            if self.LToken.token_code != self.LToken.RPAREN:
                self.error()
            return

        else:
            self.error()
        




