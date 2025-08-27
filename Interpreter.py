import re
import sys
import traceback

# Custom input functions for Pylang
def intput(prompt: str) -> int:
    return int(input(prompt))

def strput(prompt: str) -> str:
    return input(prompt)

# Constant handler
class Const:
    def __init__(self):
        self._constants = {}

    def define(self, name, value):
        if name in self._constants:
            raise ValueError(f"Cannot reassign constant '{name}'")
        self._constants[name] = value
        globals()[name] = value

# Convert Go-style function parameters with type hints to Python
def convert_params(param_str):
    params = param_str.split(',')
    converted = []
    for param in params:
        parts = param.strip().split()
        if len(parts) == 2:
            name, type_ = parts
            converted.append(f"{name}: {type_}")
        else:
            converted.append(parts[0])
    return ', '.join(converted)


# Function to run Pylang code from a .pyl file
def run_pylang_file(filename: str):
    with open(filename, 'r') as file:
        content = file.read()

    # Check for forbidden Python keywords in Pylang
    forbidden_keywords = {
        'def': "Use 'func' instead of 'def'",
        'while': "Use 'for' loops instead of 'while'",
        'class': "Classes are not supported in Pylang"
    }

    for keyword, message in forbidden_keywords.items():
        if re.search(rf'\b{re.escape(keyword)}\b', content):
            raise SyntaxError(f"Forbidden keyword: '{keyword}' → {message}")

    # Check for forbidden '#' comments
    if re.search(r'^\s*#', content, flags=re.MULTILINE):
        raise SyntaxError("Forbidden character: '#' → Use '//' for comments instead of '#'")

    # Remove multi-line comments (/* ... */)
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    # Convert Go-style comments (//) to Python-style comments (#)
    content = re.sub(r'^\s*//', '#', content, flags=re.MULTILINE)

    # Convert const declaration to define_const call
    content = re.sub(r'\bconst\s+(\w+)\s*=\s*(.+)', r'define_const("\1", \2)', content)

    # Convert 'var x = 5' to 'x = 5'
    content = re.sub(r'\bvar\s+(\w+)\s*=\s*(.+)', r'\1 = \2', content)

    # Convert 'func name(a int, b str) int {' to 'def name(a: int, b: str) -> int:'
    content = re.sub(
        r'func\s+(\w+)\s*\((.*?)\)\s*(\w+)?\s*{',
        lambda m: f"def {m.group(1)}({convert_params(m.group(2))})" +
                  (f" -> {m.group(3)}" if m.group(3) else "") + ":",
        content
    )

    # Convert any remaining 'func name(...) {' to 'def name(...):'
    content = re.sub(r'func\s+(\w+)\s*\((.*?)\)\s*{', r'def \1(\2):', content)

    # Convert Println to print
    content = re.sub(r'\bPrintln\b', 'print', content)


    # Prepare execution environment
    consts = Const()
    exec_env = {
        'input_int': intput,
        'input_str': strput,
        'define_const': consts.define
    }

    # Execute the translated Python code
    try:
        exec(content, exec_env)
        if 'main' in exec_env:
            exec_env['main']()
    except Exception as e:
        print(f"Pylang cannot be run due to an error: {e}")
        traceback_lines = traceback.format_exc().splitlines()
        for line in traceback_lines:
            print(line)

# Entry point for the script
if len(sys.argv) != 2:
    print("Usage: python script.py <filename.pyl>")
else:
    filename = sys.argv[1]
    if filename.endswith('.pyl'):
        run_pylang_file(filename)
    else:
        print("Error: The file must have a .pyl extension.")
