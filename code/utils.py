def binary_to_int(bits):
    # Convert binary text like "1010" to an integer.
    return int(bits, 2)


def sign_extend(bits):
    # Interpret the binary text as a signed two's-complement value.
    value = int(bits, 2)
    width = len(bits)
    if bits[0] == "1":
        value -= 1 << width
    return value


def reg_name(index):
    # Project format uses R0, R1, R2, ... for register names.
    return f"R{index}"


def format_bits(bits):
    # Display instruction bits in grouped fields for readability.
    return (
        f"{bits[:6]} {bits[6:11]} {bits[11:16]} "
        f"{bits[16:21]} {bits[21:26]} {bits[26:]}"
    )
