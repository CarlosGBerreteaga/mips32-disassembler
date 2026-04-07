# MIPS Decoder CLI

This project is a MIPS instruction/data decoder for CMPS-6510 that reads a text file of 32-bit binary lines, disassembles instruction lines, and writes the decoded output while also printing the same results to the terminal.

Run format:
`python mips_decoder.py <inputfilename> <outputfilename>`

Note: `test_inputs/test1.txt` was AI-generated based on the assignment requirements.

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
