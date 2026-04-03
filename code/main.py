from decoder import decode_i_type
from utils import format_bits, sign_extend_32

def run(input_file, output_file):
    address = 496
    data_section = False

    with open(input_file) as f, open(output_file, "w") as out:
        for line in f:
            b = line.strip()
            if not b:
                continue

            if not data_section:
                decoded = decode_i_type(b, address)

                out.write(f"{format_bits(b)}\t{address}\t")

                if "\t" in decoded:
                    op, rest = decoded.split("\t")
                    out.write(f"{op}\t{rest}\n")
                else:
                    out.write(f"{decoded}\n")

                if decoded == "BREAK":
                    data_section = True

            else:
                value = sign_extend_32(b)
                out.write(f"{b}\t{address}\t{value}\n")

            address += 4

if __name__ == "__main__":
    import sys
    run(sys.argv[1], sys.argv[2])