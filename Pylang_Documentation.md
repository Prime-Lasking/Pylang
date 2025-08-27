# 🐍 Pylang Interpreter

Pylang is a lightweight Python-based interpreter for a custom
programming language that blends Python's flexibility with
Golang-inspired syntax. Designed as a learning tool and experimental
language, Pylang offers a simplified syntax layer that compiles to
standard Python under the hood.

------------------------------------------------------------------------

## 🚀 Features

-   Golang-like syntax with Python execution\
-   Simple translation from `.pyl` source code to native Python\
-   Basic input/output capabilities\
-   Familiar Python functionality with stricter syntactic rules\
-   Custom comment and function declaration styles

------------------------------------------------------------------------

## 📦 Installation

Clone the repository and run the interpreter:

``` bash
git clone https://github.com/yourusername/pylang.git
cd pylang
python pylang.py examples/hello.pyl
```

------------------------------------------------------------------------

## 🧾 Syntax Overview

### Comments

``` pyl
// This is a comment
```

### Functions

``` pyl
func greet():
    Println("Hello from Pylang!")
```

Becomes:

``` python
def greet():
    print("Hello from Pylang!")
```

### Printing

``` pyl
Println("Hello, World!")
```

Becomes:

``` python
print("Hello, World!")
```

### Input

``` pyl
name = input_str("Enter your name: ")
Println("Hello, " + name)
```

Becomes:

``` python
name = input("Enter your name: ")
print("Hello, " + name)
```

------------------------------------------------------------------------

## 📂 Example Program

Pylang code (`example.pyl`):

``` pyl
// Simple program in Pylang

func greet():
    Println("Welcome to Pylang!")

func main():
    name = input_str("Enter your name: ")
    Println("Hello, " + name + "!")

greet()
main()
```

Equivalent Python code:

``` python
# Simple program in Pylang

def greet():
    print("Welcome to Pylang!")

def main():
    name = input("Enter your name: ")
    print("Hello, " + name + "!")

greet()
main()
```

Run it with:

``` bash
python pylang.py example.pyl
```

------------------------------------------------------------------------

## 🛠 Future Improvements

-   Typed variables (`int x = 5`)\
-   Package imports\
-   Loop and conditional syntax inspired by Go\
-   Error handling for invalid syntax

------------------------------------------------------------------------

## 📜 License

MIT License © 2025 Your Name
