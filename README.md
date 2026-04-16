# MIPS Decoder CLI

This project is a MIPS instruction/data decoder for CMPS-6510 that reads a text file of 32-bit binary lines, disassembles instruction lines, and writes the decoded output while also printing the same results to the terminal.

Run format:
`python mips_decoder.py <inputfilename> <outputfilename>`

Note: `test_inputs/test1.txt` was AI-generated based on the assignment requirements.

## Function Breakdown By File

`mips_decoder.py`
- No user-defined functions in this file. It acts as a launcher that imports and calls `main()` from `code/main.py`.

`code/main.py`
- `print_banner()`: Prints the ASCII title and project info shown at startup.
- `print_input_requirements()`: Prints the required input file format rules.
- `validate_binary_line(bits, line_number)`: Checks that each non-empty input line is exactly 32 bits and only uses `0`/`1`.
- `run(input_file, output_file)`: Main processing loop that reads the input file, decodes instructions/data, writes output, and prints the same lines to CLI.
- `main()`: Handles command-line arguments, shows usage/errors, and starts the program.

`code/decoder.py`
- `format_instruction(opcode, operands="")`: Builds the instruction text format used in the output columns.
- `decode_r_type(bits)`: Decodes R-type instructions by reading `funct` and related register/shift fields.
- `decode_instruction(bits)`: Decodes one 32-bit instruction word by opcode (and calls `decode_r_type` when needed).

`code/utils.py`
- `binary_to_int(bits)`: Converts a binary string to an integer.
- `sign_extend(bits)`: Converts a binary string to a signed two's-complement integer.
- `reg_name(index)`: Formats register numbers as `R#` names (for example `R8`).
- `format_bits(bits)`: Splits a 32-bit instruction into grouped fields for readable output.

## References (Documentation Links)

Official Python docs for less-common functions/modules used in this project:

- `pathlib.Path.resolve()`: Converts a path to an absolute, normalized path.  
  Reference: https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve
- `sys.path`: The module search path list Python uses when importing files.  
  Reference: https://docs.python.org/3/library/sys.html#sys.path
- `list.insert()`: Inserts an item into a list at a specific index (used by `sys.path.insert(...)`).  
  Reference: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
- `subprocess.run()`: Runs another program/command from Python (used in test runner).  
  Reference: https://docs.python.org/3/library/subprocess.html#subprocess.run
- `os.path.join()`: Joins path pieces safely for the current operating system.  
  Reference: https://docs.python.org/3/library/os.path.html#os.path.join
- `os.path.basename()`: Returns just the filename part of a path.  
  Reference: https://docs.python.org/3/library/os.path.html#os.path.basename
- `enumerate()`: Loops over an iterable while also getting an index counter.  
  Reference: https://docs.python.org/3/library/functions.html#enumerate
- `open()`: Opens a file for reading or writing.  
  Reference: https://docs.python.org/3/library/functions.html#open

## Development Process

1. Defined the decoder scope for CMPS-6510 requirements: instruction decoding, data section handling, and fixed address progression.
2. Implemented helper functions for binary conversion, sign extension, register naming, and bit formatting.
3. Built instruction decoding logic for supported R-type and I-type operations.
4. Implemented file I/O flow to read binary input lines and write decoded results.
5. Added command-line argument support for input and output paths.
6. Added input validation (32-bit lines, binary-only characters) and runtime error handling.
7. Added a startup banner with project/course metadata and validated behavior with test input files.
8. Finalized the command-line interface to run directly with Python arguments.

## Tools Used (Non-AI)

- Python 3.11
- PowerShell (Windows CLI)
- VS Code
- Standard Python libraries (`sys`, file I/O)
