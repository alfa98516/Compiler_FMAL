from ltoken import LToken
from llexer import LLexer

if __name__ == "__main__":
    lexer = LLexer()
    curr_token = LToken("",-1)
    counter = 0
    while curr_token.token_code != LToken.END and counter < 20:
        
        curr_token = lexer.get_next_token()
        print(curr_token)
        counter+=1
