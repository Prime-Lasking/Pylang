import re

# Built-in functions for Pylang
def input_int(prompt: str) -> int:
    return int(input(prompt))

def input_str(prompt: str) -> str:
    return input(prompt)

# Read Pylang source code
with open('Pylang.txt', 'r') as file:
    content = file.read()

forbidden_keywords = {
    'def': "Use 'func' instead of 'def'",
    'while': "Use 'for' loops instead of 'while'",
    'class': "Classes are not supported in Pylang",
}

for keyword, message in forbidden_keywords.items():
    if re.search(rf'\b{re.escape(keyword)}\b', content):
        raise SyntaxError(f"Forbidden keyword: '{keyword}' → {message}")

content = re.sub(r'\bfunc\b', 'def', content)
content = re.sub(r'\bPrintln\b', 'print', content)

exec(content)
