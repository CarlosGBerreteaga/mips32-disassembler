def binary_to_int(bits):
    # Convert binary text (like "1010") to int.
    return int(bits, 2)


def sign_extend(bits):
    # Read a binary string as signed two's-complement.
    # If the first bit is 1, it is negative.
    value = int(bits, 2)
    width = len(bits)
    if bits[0] == "1":
        value -= 1 << width
    return value


def reg_name(index):
    # Output register name as R0, R1, R2, etc.
    return f"R{index}"


def format_bits(bits):
    # Split 32 bits into 6-5-5-5-5-6 groups for display.
    return (
        f"{bits[:6]} {bits[6:11]} {bits[11:16]} "
        f"{bits[16:21]} {bits[21:26]} {bits[26:]}"
    )
