import re
import sys
import traceback

# Custom input functions for Pylang
def intput(prompt: str) -> int:
    return int(input(prompt))

def strput(prompt: str) -> str:
    return input(prompt)

# Function to run Pylang code from a .pyl file
def run_pylang_file(filename: str):
    with open(filename, 'r') as file:
        content = file.read()

    forbidden_keywords = {
        'def': "Use 'func' instead of 'def'",
        'while': "Use 'for' loops instead of 'while'",
        'class': "Classes are not supported in Pylang",
    }

    for keyword, message in forbidden_keywords.items():
        if re.search(rf'\b{re.escape(keyword)}\b', content):
            raise SyntaxError(f"Forbidden keyword: '{keyword}' → {message}")

    conversion_keywords = {
        "func": "def",
        "Println": "print"
    }
    for old_keyword, new_keyword in conversion_keywords.items():
        content = re.sub(r'\b' + old_keyword + r'\b', new_keyword, content)

    try:
        exec(content, {'input_int': input_int, 'input_str': input_str})
    except Exception:
        print("Pylang cannot be run due to an error:")
        traceback_lines = traceback.format_exc().splitlines()
        for line in traceback_lines:
            print(line)

if len(sys.argv) != 2:
    print("Usage: python script.py <filename.pyl>")
else:
    filename = sys.argv[1]
    if filename.endswith('.pyl'):
        run_pylang_file(filename)
    else:
        print("Error: The file must have a .pyl extension.")
