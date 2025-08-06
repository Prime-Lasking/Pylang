import re
import sys

# Custom input functions for Pylang
def input_int(prompt: str) -> int:
    return int(input(prompt))

def input_str(prompt: str) -> str:
    return input(prompt)

# Function to run Pylang code from a .pyl file
import re

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
        exec(content)
    except Exception as e:
        print(f"Pylang cannot be run. Error: {type(e).__name__} - {e}")
        

if len(sys.argv) != 2:
    print("Usage: python script.py <filename.pyl>")
else:
    filename = sys.argv[1]
    if filename.endswith('.pyl'):
        run_pylang_file(filename)
    else:
        print("Error: The file must have a .pyl extension.")
