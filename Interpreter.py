#!/usr/bin/env python3
import re
import sys
import traceback

def pylang_interpreter():
    def intput(prompt: str) -> int:
        return int(input(prompt))

    def strput(prompt: str) -> str:
        return input(prompt)

    if len(sys.argv) != 2:
        print("Usage: python script.py <filename.pyl>")
        return

    filename = sys.argv[1]
    if not filename.endswith('.pyl'):
        print("Error: The file must have a .pyl extension.")
        return

    try:
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return

    # Check for forbidden keywords
    forbidden_keywords = {
        'def': "Use 'func' instead of 'def'",
        'while': "Use 'for' loops instead of 'while'",
        'class': "Classes are not supported in Pylang"
    }

    for keyword, message in forbidden_keywords.items():
        if re.search(rf'\b{re.escape(keyword)}\b', content):
            print(f"SyntaxError: Forbidden keyword: '{keyword}' → {message}")
            return

    # Reject Python-style comments
    if re.search(r'^\s*#', content, flags=re.MULTILINE):
        print("SyntaxError: Forbidden character: '#' → Use '//' for comments instead")
        return

    # Translate Pylang to Python
    try:
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)          # Remove multi-line comments
        content = re.sub(r'^\s*//', '#', content, flags=re.MULTILINE)         # Convert // to #
        content = re.sub(r'\bfunc\b', 'def', content)                         # func → def
        content = re.sub(r'\bPrintln\b', 'print', content)                   # Println → print
    except Exception as e:
        print(f"Error while translating code: {e}")
        return

    exec_env = {
        'input_int': intput,
        'input_str': strput,
    }

    try:
        exec(content, exec_env)
    except Exception as e:
        print(f"Pylang cannot be run due to an error: {e}")
        traceback_lines = traceback.format_exc().splitlines()
        for line in traceback_lines:
            print(line)

# Run the interpreter
pylang_interpreter()
