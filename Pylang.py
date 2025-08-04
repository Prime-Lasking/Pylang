
def intput(x:int):
     return int(input(x))
def strput(x:str):
    return str(input(x))
with open('Pylang.txt', 'r') as file:
    content = file.read()
if "def" in content:
    raise SyntaxError("Do you mean to use func")
if "=" in content:
    raise SyntaxError("Do you mean to use :=")
if 'while' in content:
    raise TypeError("No while loops,only for loops, it's Pylang")
content = content.replace('func','def')
content = content.replace(':=','=')
content = content.replace('Println','print')
exec(content)
