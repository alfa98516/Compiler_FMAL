import sys
from LLexer import LLexer
from LToken import LToken


# Statements -> Statement ; Statements | end
# Statement -> id = Expr | print id
# Expr- > Term | Term + Expr | Term – Expr
# Term -> Factor | Factor * Term
# Factor -> int | id | ( Expr ) 


class LParser:
    def __init__(self, lexer):
        self.extra = False
        self.LLexer = lexer
        self.LToken = None

    def parser(self):
        self.next_token()
        self.statements()
        print()

    def error(self):
        print("Syntax error")
        sys.exit(1)

    def next_token(self):
        if self.extra: # If a function calls next token but did not need it.
            self.extra = False
            return

        token = self.LLexer.get_next_token()

        if token.token_code == token.ERROR:
            print("invalid token")
            self.error()
        self.LToken = token

    def statements(self):
 
        if self.LToken.token_code == self.LToken.END:
            return
        
        self.statement()
        self.next_token()
        
        if (self.LToken.lexeme != self.LLexer.SEMICOL):
            self.error()

        self.next_token()
        self.statements() 
    
    def statement(self):
        
        
        if self.LToken.token_code == self.LToken.END:
            self.error()

        if self.LToken.token_code == self.LToken.PRINT:
            self.next_token()
            if self.LToken.token_code != self.LToken.ID:
                self.error()

            print(f"PUSH {self.LToken.lexeme}")
            print("PRINT")

            return
        
        if self.LToken.token_code == self.LToken.ID:
            print(f"PUSH {self.LToken.lexeme}")
            self.next_token()

            if self.LToken.lexeme != self.LLexer.ASSIGN:
                self.error()

            self.next_token()
            self.expression()
            print("ASSIGN")
            return

        else:
            self.error()

            
    def expression(self):
        self.term()
        self.next_token()

        if self.LToken.token_code == self.LToken.SEMICOL:
            self.extra = True
            return

        elif self.LToken.token_code == self.LToken.PLUS:
            self.next_token()
            self.expression()
            
            if self.LToken.token_code != self.LToken.SEMICOL:
                self.error()

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
            self.extra = True
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
        




