from __init__ import *
from Lexer import *
from Parser import *
from Interpreter import *
from S import *

def run(fn, text):
  # Generate tokens
  lexer = Lexer(fn, text)
  tokens, error = lexer.make_tokens()
  if error: return None, error
  
  # Generate AST
  parser = Parser(tokens)
  ast = parser.parse()
  
  if ast.error: return None, ast.error

  # Run program
  interpreter = Interpreter()
  context = Context('<program>')
  context.symbol_table = global_symbol_table
  result = interpreter.visit(ast.node, context)

  return result.value, result.error
line=0
if __name__ == "__main__":
    while True:
        line += 1
        
        try:
            text = input('{%s}=>' % line).strip()



            if text == "":
                continue
            elif text=="EXIT()":
                sys.exit()

            result, error = run('<stdin>', text)
        except (EOFError,KeyboardInterrupt):
            print('KeyboardInterrupt')
            continue
        if error:
                print(error.as_string())
        elif result:
            if isinstance(result, List) and len(result.elements) == 1:
                print(repr(result.elements[0]))
            else:
                print(repr(result))
