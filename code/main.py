import sys

from decoder import decode_i_type
from utils import format_bits, sign_extend_32

VERSION = "1.0.0"


def print_banner():
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
    print("Input file requirements:")
    print("1. Plain text file")
    print("2. One 32-bit binary value per non-empty line")
    print("3. Only characters '0' and '1' are allowed")
    print()


def validate_binary_line(bits, line_number):
    if len(bits) != 32 or any(ch not in ("0", "1") for ch in bits):
        raise ValueError(
            f"Invalid input on line {line_number}: each non-empty line must be 32 bits (0/1 only)."
        )


def run(input_file, output_file):
    address = 496
    data_section = False

    with open(input_file) as f, open(output_file, "w") as out:
        for line_number, line in enumerate(f, start=1):
            b = line.strip()
            if not b:
                continue
            validate_binary_line(b, line_number)

            if not data_section:
                decoded = decode_i_type(b, address)
                prefix = f"{format_bits(b)}\t{address}\t"
                if "\t" in decoded:
                    op, rest = decoded.split("\t")
                    output_line = f"{prefix}{op}\t{rest}"
                else:
                    output_line = f"{prefix}{decoded}"

                if decoded == "BREAK":
                    data_section = True

            else:
                value = sign_extend_32(b)
                output_line = f"{b}\t{address}\t{value}"

            out.write(output_line + "\n")
            print(output_line)
            address += 4

def main():
    if len(sys.argv) > 1:
        print("This program does not accept command-line flags or arguments.")
        print("Run: python code/main.py")
        sys.exit(2)

    print_banner()
    print_input_requirements()
    input_file = input("Enter input file path: ").strip()
    output_file = input("Enter output file path: ").strip()
    print()

    if not input_file or not output_file:
        print("Error: both input and output file paths are required.")
        sys.exit(2)

    try:
        run(input_file, output_file)
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    except ValueError as exc:
        print(f"Error: {exc}")
        sys.exit(1)


if __name__ == "__main__":
    main()
