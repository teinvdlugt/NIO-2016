def decode(code):
    for i in range(2, len(code) + 1):
        g = len(code) - i + 2
        if len(code) % g == 0:
            new_code = ""
            for j in range(0, len(code)):
                if (j + 1) % g == 0:
                    new_code += code[(j + 1) / g - 1]
                else:
                    new_code += code[len(code) / g - 1 + (j + 1) - (j + 1) / g]
            code = new_code
    return code


def encode(text):
    for g in range(2, len(text) + 1):
        if len(text) % g == 0:
            new_text_begin = ""
            new_text_end = ""
            for i in range(0, len(text)):
                if (i + 1) % g == 0:
                    new_text_begin += text[i]
                else:
                    new_text_end += text[i]
            text = new_text_begin + new_text_end

    return text

code = encode(raw_input("Input: "))
print code
print decode(code)
