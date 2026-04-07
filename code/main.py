import os
import sys

from decoder import decode_instruction
from utils import format_bits, sign_extend

# Simple version tag shown in the banner.
VERSION = "1.0.0"


def print_banner():
    # Startup title shown every time the program runs.
    banner = r"""
 __  __ ___ ____  ____    ____  _____ ____ ___  ____  _____ ____
|  \/  |_ _|  _ \/ ___|  |  _ \| ____/ ___/ _ \|  _ \| ____|  _ \
| |\/| || || |_) \___ \  | | | |  _|| |  | | | | | | |  _| | |_) |
| |  | || ||  __/ ___) | | |_| | |__| |__| |_| | |_| | |___|  _ <
|_|  |_|___|_|   |____/  |____/|_____\____\___/|____/|_____|_| \_\
"""
    print(banner)
    print("Project: MIPS Decoder CLI")
    print(f"Version: {VERSION}")
    print("Coded by Carlos Berreteaga | Date: 06 APR 26")
    print("School: Tulane University | Class: CMPS-6510: Computer Organization")
    print()


def print_input_requirements():
    # Quick rules so the user knows what kind of file to provide.
    print("Input file requirements:")
    print("1. Plain text file")
    print("2. One 32-bit binary value per non-empty line")
    print("3. Only characters '0' and '1' are allowed")
    print()


def validate_binary_line(bits, line_number):
    # Every non-empty line must be exactly 32 binary characters.
    if len(bits) != 32 or any(ch not in ("0", "1") for ch in bits):
        raise ValueError(
            f"Invalid input on line {line_number}: each non-empty line must be 32 bits (0/1 only)."
        )


def run(input_file, output_file):
    # Assignment output starts addresses at 496 and moves by 4 each line.
    address = 496
    # Before BREAK we decode instructions, after BREAK we treat lines as data.
    data_section = False

    # Read input and write output at the same time.
    with open(input_file) as f, open(output_file, "w") as out:
        for line_number, line in enumerate(f, start=1):
            bits = line.strip()
            if not bits:
                # Skip blank lines to avoid noisy errors.
                continue
            validate_binary_line(bits, line_number)

            if not data_section:
                # Instruction part: decode the binary instruction text.
                decoded = decode_instruction(bits)
                output_line = f"{format_bits(bits)}\t{address}\t{decoded}"
                if decoded == "BREAK":
                    # Once BREAK is seen, later lines are data values.
                    data_section = True
            else:
                # Data part: convert signed 32-bit binary to decimal.
                value = sign_extend(bits)
                output_line = f"{bits}\t{address}\t{value}"

            # Keep file output and terminal output exactly the same.
            out.write(output_line + "\n")
            print(output_line)
            address += 4

def main():
    # Required interface: input file and output file are positional args.
    if len(sys.argv) != 3:
        script_name = os.path.basename(sys.argv[0]) if sys.argv else "mips_decoder.py"
        print(f"Usage: python {script_name} <inputfilename> <outputfilename>")
        print(f"Example: python {script_name} input/fibbonaci_bin.txt output/result.txt")
        print()
        print_input_requirements()
        sys.exit(2)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    print_banner()

    try:
        run(input_file, output_file)
    except FileNotFoundError as exc:
        # Common file path mistake.
        print(f"Error: {exc}")
        sys.exit(1)
    except ValueError as exc:
        # Input file format problem (line length / non-binary chars).
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
