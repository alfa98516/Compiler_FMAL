class LToken:
    ID = 0
    ASSIGN = 1
    SEMICOL = 3
    INT = 4
    PLUS = 5
    MINUS = 6
    MULT = 7
    LPAREN = 8
    RPAREN = 9
    PRINT = 10
    END = 11
    ERROR = 12

    def __init__(self, lexeme, token_code):
        self.lexeme = lexeme
        self.token_code = token_code
    def __str__(self):
        return f"{self.lexeme} : {self.token_code}"
