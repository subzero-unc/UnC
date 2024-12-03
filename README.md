# UnC++

UnC++ is a lightweight and experimental programming language designed for simplicity and learning. It provides a basic syntax for input, output, and delays, making it great for small projects or as an introduction to programming concepts.

---

## Features
- **Simple Syntax**: Easy to learn and write.
- **Customizable**: Users can modify or extend UnC++.
- **Interactive**: Supports user input, output, and execution delays.
- **Open Source**: Contributions are welcome!

---

## Installation
### Requirements
- Python 3.x
- Nuitka (for compiling UnC++ code)

### Steps
1. Clone this repository or download it as a ZIP file.
2. Install dependencies running install.bat
3. You're ready to use UnC++!

## Usage
### Writing UnC++ Code
write your UnC++ code in a .unc file. Example:
```
namespace Main {
    act main() {
        let name = input("What is your name? ");
        prnt("Hello, " + name + "!");
        dly(2);
        prnt("Goodbye!");
    }
}
```
# Running UnC++ Code
1. Use the UnC++ compiler to compile your code:
python unc_compiler.py
2. Replace the code in input.unc with your own code to experiment!

# Contributing
- Fork this repository.
- Create your branch.
- Submit a pull request with your changes.

# License
This project is licensed under the UnC++ License. By using or contributing, you agree to its terms.

UnC++ was created by Subzero. Join the community and share your custom versions of UnC++!