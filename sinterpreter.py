import sys
from llexer import LLexer
class SInterpreter:
    def __init__(self):
        self.stack = []
        self.vars = {}
 
    def cycle(self):
        for line in sys.stdin:
            argv = line.split()
            if not argv:
                quit()

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
                continue

            if arg1 == "ASSIGN":
                self.assign()
                continue

            if arg1 == "PRINT":
                self.stackPrint()
                continue
            else:
                self.error(arg1)

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

            self.error("ADD")

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
            self.error("SUB")

    def stackPrint(self):
        try:
            a = self.stack.pop()
            val = self.vars[a]
        except IndexError and KeyError:
            self.error("PRINT")
        print(val)

    def push(self, val):
        try:
            val = int(val)
        except ValueError:
            self.vars[val] = 0

        self.stack.append(val)
        
    def assign(self):
        val = self.stack.pop()
        var = self.stack.pop()
        try:
            val = self.vars[val]
        except KeyError:
            pass
        
        if type(val) == int:
            self.vars[var] = val
        else:
            self.error("ASSIGN")

        
    def mult(self):
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
            self.push(int(a) * int(b))
        except ValueError:
            self.error("MULT")
    
    def error(self, operator):
        print(f"Error for operator: {operator}")
        quit(0)

if __name__ == "__main__":
    interpreter = SInterpreter()
    interpreter.cycle()
