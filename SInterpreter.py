import sys
from LLexer import LLexer
class SInterpreter:
    def __init__(self):
        self.stack = []
        self.vars = {}
 
    def cycle(self):
        for line in sys.stdin:
            argv = line.split() 
            arg1 = argv[0]
            arg2 = ""

            if len(argv) == 2:
                arg2 = argv[1]
            

            if arg1 == "PUSH":
                if arg2:
                    self.push(arg2)
                    continue

                else:
                    self.error()

            if arg1 == "ADD":
                self.add()
                continue
            
            if arg1 == "SUB":
                self.sub()
                continue
            
            if arg1 == "MULT":
                self.mult()
            
            if arg1 == "ASSIGN":
                self.assign()
            

            if arg1 == "PRINT":
                self.stackPrint()
            
            if line.strip() == "Syntax error":
                self.error()
            
    def add(self):
        
        a = self.stack.pop()
        
        try:
            a = self.vars[a]
        except KeyError:
            pass

        
        b = self.stack.pop()
        
        try:
            b = self.vars[b]
        except KeyError:
            pass

        try:
            self.push(int(a)+int(b))

        except ValueError:
            self.error()

    def sub(self):
        a = self.stack.pop()
        
        try:
            a = self.vars[a]
        
        except KeyError:
            pass

        
        b = self.stack.pop()
        
        try:
            b = self.vars[b]
        except KeyError:
            pass

        try:
            self.push(int(a)-int(b))
        except ValueError:
            self.error()

    def stackPrint(self):
        try:
            a = self.stack.pop()
            val = self.vars[a]
        except IndexError and KeyError:
            self.error()
        print(a)

    def push(self, val):
        try:
            val = int(a)
        except ValueError:
            pass

        self.stack.append(val)
        
    def assign(self):
        var = self.stack.pop()
        val = self.stack.pop()

        try:
            val = self.vars[val]
        except KeyError:
            pass
        
        if type(val) == int:
            self.vars[var] = val

        else:
            self.error()
        
    
        

        

    def mult(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.push(a * b)
    
    def error(self):
        print("Syntax error")
        sys.exit(1)

if __name__ == "__main__":
    interpreter = SInterpreter()
    interpreter.cycle()
