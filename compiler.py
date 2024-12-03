import re
import subprocess
import os

def translate(code, debug=False):
    rules = {
        r"namespace ([\w:]+) \{": lambda m: f"class {m.group(1).replace(':', '_')}:",
        r"class (\w+) \{": r"class \1:",
        r"constructor\((.*)\)": r"def __init__(self, \1):",
        r"self->": "self.",
        r"->": ".",
        r"new ([\w:]+)": lambda m: m.group(1).replace("::", "_"),
        r"([\w:]+)::([\w]+)": lambda m: f"{m.group(1).replace(':', '_')}.{m.group(2)}",
        r"act (\w+)\((.*)\)": r"def \1(self, \2):",
        r"lp \((\w+) in (\d+)\.\.(\d+)\)": r"for \1 in range(\2, \3 + 1):",
        r"prnt\((.*)\)": r"print(''.join(map(str, [\1])))",
        r"let (\w+) = (.*);": r"\1 = \2",
        r"dly\((.*)\)": r"time.sleep(\1)",
        r";": "",
        r"\{": "",
        r"\}": ""
    }

    try:
        translated = code
        for pattern in rules.keys():
            replacement = rules[pattern]
            translated = re.sub(pattern, replacement, translated)

        headers = "import random\nimport time\n"
        translated = headers + translated

        if "class Main" in translated:
            if "def main" in translated:
                translated += "\n\nif __name__ == '__main__':\n    Main().main()"

        if debug:
            print("Translated Python Code:\n", translated)

        return translated
    except Exception as translation_error:
        print(f"Translation error occurred: {translation_error}")
        return None

def compile_to_exe(source_file, output="UnC++"):
    try:
        with open(source_file, "r") as file:
            raw_code = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' was not found.")
        return

    if "namespace Main" not in raw_code:
        print("Error: Missing 'namespace Main' in the input code.")
        return
    if "act main" not in raw_code:
        print("Error: Missing 'act main()' in the input code.")
        return

    py_code = translate(raw_code, debug=True)
    if py_code is None:
        print("Error: Translation failed. Compilation aborted.")
        return

    py_file = f"{output}.py"
    try:
        with open(py_file, "w") as python_file:
            python_file.write(py_code)
    except IOError as file_error:
        print(f"Error writing the translated Python code: {file_error}")
        return

    try:
        print("Starting compilation process using Nuitka...")
        subprocess.run(
            ["python", "-m", "nuitka", "--onefile", py_file],
            check=True
        )
        print("Compilation finished successfully.")
        os.system("cls")
        print(f"Executable has been created: './{output}.exe'")
    except subprocess.CalledProcessError as compilation_error:
        print(f"Compilation error: {compilation_error}")
    except Exception as general_error:
        print(f"Unexpected error during compilation: {general_error}")

    temporary_files = ["__pycache__", py_file]
    for temp in temporary_files:
        try:
            if os.path.isdir(temp):
                os.rmdir(temp)
            elif os.path.exists(temp):
                os.remove(temp)
        except Exception as cleanup_error:
            print(f"Error during cleanup: {cleanup_error}")

if __name__ == "__main__":
    default_output_name = "UnC++"
    user_defined_name = input(f"Enter the name of the output executable (default: {default_output_name}): ")
    executable_name = user_defined_name if user_defined_name.strip() else default_output_name
    compile_to_exe("input.unc", executable_name)
