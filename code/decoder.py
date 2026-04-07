from utils import binary_to_int, reg_name, sign_extend


def format_instruction(opcode, operands=""):
    # Builds output like "ADD\tR1, R2, R3".
    if operands:
        return f"{opcode}\t{operands}"
    return opcode


def decode_r_type(bits):
    # R-type fields come from fixed bit slices.
    rs = binary_to_int(bits[6:11])
    rt = binary_to_int(bits[11:16])
    rd = binary_to_int(bits[16:21])
    shamt = binary_to_int(bits[21:26])
    funct = binary_to_int(bits[26:32])

    # funct decides which R-type instruction this is.
    if funct == 0:
        # All zeros means NOP in this project.
        if rs == 0 and rt == 0 and rd == 0 and shamt == 0:
            return "NOP"
        return format_instruction("SLL", f"{reg_name(rd)}, {reg_name(rt)}, #{shamt}")
    if funct == 2:
        return format_instruction("SRL", f"{reg_name(rd)}, {reg_name(rt)}, #{shamt}")
    if funct == 3:
        return format_instruction("SRA", f"{reg_name(rd)}, {reg_name(rt)}, #{shamt}")
    if funct == 8:
        return format_instruction("JR", reg_name(rs))
    if funct == 13:
        return "BREAK"
    if funct == 32:
        return format_instruction("ADD", f"{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}")
    if funct == 33:
        return format_instruction("ADDU", f"{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}")
    if funct == 34:
        return format_instruction("SUB", f"{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}")
    if funct == 35:
        return format_instruction("SUBU", f"{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}")
    if funct == 36:
        return format_instruction("AND", f"{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}")
    if funct == 37:
        return format_instruction("OR", f"{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}")
    if funct == 38:
        return format_instruction("XOR", f"{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}")
    if funct == 39:
        return format_instruction("NOR", f"{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}")
    if funct == 42:
        return format_instruction("SLT", f"{reg_name(rd)}, {reg_name(rs)}, {reg_name(rt)}")

    return "UNKNOWN R-TYPE INSTRUCTION"


def decode_instruction(bits):
    # First 6 bits are always the main opcode.
    opcode = binary_to_int(bits[:6])

    # opcode 0 means this is an R-type instruction.
    if opcode == 0:
        return decode_r_type(bits)

    # J-format uses a 26-bit target that gets shifted left by 2.
    if opcode == 2:
        target = binary_to_int(bits[6:32]) << 2
        return format_instruction("J", str(target))

    # Most I-type instructions use rs, rt, and a signed 16-bit immediate.
    rs = binary_to_int(bits[6:11])
    rt = binary_to_int(bits[11:16])
    imm = sign_extend(bits[16:32])

    if opcode == 1:
        if rt == 0:
            return format_instruction("BLTZ", f"{reg_name(rs)}, #{imm << 2}")
        if rt == 1:
            return format_instruction("BGEZ", f"{reg_name(rs)}, #{imm << 2}")
    if opcode == 4:
        return format_instruction("BEQ", f"{reg_name(rs)}, {reg_name(rt)}, #{imm << 2}")
    if opcode == 5:
        return format_instruction("BNE", f"{reg_name(rs)}, {reg_name(rt)}, #{imm << 2}")
    if opcode == 6:
        return format_instruction("BLEZ", f"{reg_name(rs)}, #{imm << 2}")
    if opcode == 7:
        return format_instruction("BGTZ", f"{reg_name(rs)}, #{imm << 2}")
    if opcode == 8:
        return format_instruction("ADDI", f"{reg_name(rt)}, {reg_name(rs)}, #{imm}")
    if opcode == 9:
        return format_instruction("ADDIU", f"{reg_name(rt)}, {reg_name(rs)}, #{imm}")
    if opcode == 10:
        return format_instruction("SLTI", f"{reg_name(rt)}, {reg_name(rs)}, #{imm}")
    if opcode == 35:
        return format_instruction("LW", f"{reg_name(rt)}, {imm}({reg_name(rs)})")
    if opcode == 43:
        return format_instruction("SW", f"{reg_name(rt)}, {imm}({reg_name(rs)})")

    return "UNKNOWN I-TYPE INSTRUCTION"
