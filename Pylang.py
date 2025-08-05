import re
# Built-in Functions
def intput(prompt: str) -> int:
    return int(input(prompt))

def strput(prompt: str) -> str:
    return input(prompt)

# Read Pylang source code
with open('Pylang.txt', 'r') as file:
    content = file.read()

# List of forbidden Python keywords
forbidden_keywords = {
    'def': "Use 'func' instead of 'def'",
    '==': "Use ':=' for comparisons in Pylang",
    'while': "Use 'for' loops instead of 'while'",
    'class': "Classes are not supported in Pylang",
}

for keyword, message in forbidden_keywords.items():
    if re.search(rf'\b{keyword}\b', content):
        raise SyntaxError(f"Forbidden keyword: '{keyword}' → {message}")

content = re.sub(r'\bfunc\b', 'def', content)
content = re.sub(r'\bPrintln\b', 'print', content)
content = re.sub(r'\s*:=\s*', ' == ', content)
# Run the converted code
exec(content)




