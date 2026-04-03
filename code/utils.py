def binary_to_int(b):
    return int(b,2)

def sign_extend_16(b):
    val = int(b, 2)

    if b[0] == '1':
        val -= (1 <<16)
    return val

def sign_extend_32(b):
    val = int(b, 2)

    if b[0] == '1':
        val -= (1 <<32)
    return val

def reg_name(r):
    # regs = [
    #     "R0","AT","V0","V1","A0","A1","A2","A3",
    #     "T0","T1","T2","T3","T4","T5","T6","T7",
    #     "S0","S1","S2","S3","S4","S5","S6","S7",
    #     "T8","T9","K0","K1","GP","SP","FP","RA"
    # ]
    return f"R{r}"

def format_bits(b):
    return b[:6] + " " + b[6:11] + " " + b[11:16] + " " + b[16:21] + " " + b[21:26] + " " + b[26:]