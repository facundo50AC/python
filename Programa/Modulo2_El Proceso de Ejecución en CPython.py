import ast

code = "a = 10 + 5"
parsed_code = ast.parse(code, mode='exec')

print(ast.dump(parsed_code, indent=4))

