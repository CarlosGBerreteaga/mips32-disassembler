from utils import *

def decode_r_type(b):
    rs = binary_to_int(b[6:11])
    rt = binary_to_int(b[11:16])
    rd = binary_to_int(b[16:21])
    shamt = binary_to_int(b[21:26])
    funct = binary_to_int(b[26:32])

    if funct == 32:
        return f"ADD  \t{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}"

    if funct == 33:
        return f"ADDU  \t{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}"

    if funct == 34:
        return f"SUB  \t{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}"

    if funct == 35:
        return f"SUBU \t{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}"

    if funct == 36:
        return f"AND   \t{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}"

    if funct == 37:
        return f"OR   \t{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}"

    if funct == 38:
        return f"XOR   \t{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}"

    if funct == 39:
        return f"NOR   \t{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}"

    if funct == 42:
        return f"SLT   \t{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}"

    if funct == 0:
        if rs == 0 and rt == 0 and rd == 0 and shamt == 0:
            return "NOP"
        return f"SLL  \t{reg_name(rd)}, {reg_name(rt)}, #{shamt}"

    if funct == 2:
        return f"SRL \t{reg_name(rd)}, {reg_name(rt)}, #{shamt}"

    if funct == 3:
        return f"SRA  \t{reg_name(rd)}, {reg_name(rt)}, #{shamt}"

    if funct == 8:
        return f"JR   \t{reg_name(rs)}"

    if funct == 13:
        return "BREAK"

    return "UNKNOWN R-TYPE INSTRUCTION"


def decode_i_type(b, address):
    opcode = binary_to_int(b[:6])

    if opcode == 0:
        return decode_r_type(b)

    if opcode == 2:
        target = binary_to_int(b[6:32]) << 2
        return f"J    \t{target}"

    rs = binary_to_int(b[6:11])
    rt = binary_to_int(b[11:16])
    imm = sign_extend_16(b[16:32])

    if opcode == 4:
        return f"BEQ \t{reg_name(rs)}, {reg_name(rt)}, #{imm << 2}"

    if opcode == 5:
        return f"BNE \t{reg_name(rs)}, {reg_name(rt)}, #{imm << 2}"

    if opcode == 8:
        return f"ADDI \t{reg_name(rt)}, {reg_name(rs)}, #{imm}"

    if opcode == 9:
        return f"ADDIU\t{reg_name(rt)}, {reg_name(rs)}, #{imm}"

    if opcode == 10:
        return f"SLTI \t{reg_name(rt)}, {reg_name(rs)}, #{imm}"

    if opcode == 35:
        return f"LW   \t{reg_name(rt)}, {imm}({reg_name(rs)})"

    if opcode == 43:
        return f"SW   \t{reg_name(rt)}, {imm}({reg_name(rs)})"

    if opcode == 1:
        if rt == 0:
            return f"BLTZ \t{reg_name(rs)}, #{imm << 2}"
        if rt == 1:
            return f"BGEZ \t{reg_name(rs)}, #{imm << 2}"

    if opcode == 6:
        return f"BLEZ \t{reg_name(rs)}, #{imm << 2}"

    if opcode == 7:
        return f"BGTZ \t{reg_name(rs)}, #{imm << 2}"

    return "UNKNOWN I-TYPE INSTRUCTION"