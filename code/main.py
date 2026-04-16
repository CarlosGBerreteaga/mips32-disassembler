import os
import sys

from decoder import decode_instruction
from utils import format_bits, sign_extend

# Version shown in the banner.
VERSION = "1.0.0"


def print_banner():
    # Print the title/info when the program starts.
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
    # Show the input file rules before running.
    print("Input file requirements:")
    print("1. Plain text file")
    print("2. One 32-bit binary value per non-empty line")
    print("3. Only characters '0' and '1' are allowed")
    print()


def validate_binary_line(bits, line_number):
    # Every non-empty line must be exactly 32 bits using only 0/1.
    if len(bits) != 32 or any(ch not in ("0", "1") for ch in bits):
        raise ValueError(
            f"Invalid input on line {line_number}: each non-empty line must be 32 bits (0/1 only)."
        )


def run(input_file, output_file):
    # Start at address 496 and move by 4 each line (assignment format).
    address = 496
    # Before BREAK = instruction section, after BREAK = data section.
    data_section = False

    # Read input and write output line by line.
    with open(input_file) as f, open(output_file, "w") as out:
        for line_number, line in enumerate(f, start=1):
            bits = line.strip()
            if not bits:
                # Ignore blank lines.
                continue
            validate_binary_line(bits, line_number)

            if not data_section:
                # Decode normal instruction lines.
                decoded = decode_instruction(bits)
                output_line = f"{format_bits(bits)}\t{address}\t{decoded}"
                if decoded == "BREAK":
                    # BREAK means the next lines are data values.
                    data_section = True
            else:
                # Convert data lines from 32-bit binary to signed decimal.
                value = sign_extend(bits)
                output_line = f"{bits}\t{address}\t{value}"

            # Keep file output and CLI output the same.
            out.write(output_line + "\n")
            print(output_line)
            address += 4

def main():
    # Expected command:
    # python mips_decoder.py <inputfilename> <outputfilename>
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
        # Usually a bad path or missing file.
        print(f"Error: {exc}")
        sys.exit(1)
    except ValueError as exc:
        # Raised when a line is not valid 32-bit binary.
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
