#Useful built in functions
def intput(x: int):
     return int(input(x))
def strput(x: str):
    return str(input(x))
# Loads the writing file
with open('Pylang.txt', 'r') as file:
    content = file.read()
# Starts errors for incorrect syntax
if "def" in content:
    raise SyntaxError("Do you mean to use func")
if "=" in content:
    raise SyntaxError("Do you mean to use :=")
if 'while' in content:
    raise TypeError("No while loops,only for loops, it's Pylang")
# Converts to Python by replacing
content = content.replace('func','def')
content = content.replace(':=','=')
content = content.replace('Println','print')
#Starts the program
exec(content)


