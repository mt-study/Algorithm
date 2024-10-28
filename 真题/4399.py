# 摩斯电码字典，包含0-9的对应关系
morse_code = {
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}

# 反向字典，将摩斯电码映射到数字
morse_to_digit = {v: k for k, v in morse_code.items()}

# 要解析的摩斯电码字符串
morse_string = "....- ...-- ----. ----. -.... -.... -...."

# 将摩斯电码字符串分割为单个摩斯字符
morse_chars = morse_string.split()

# 解析摩斯电码为数字
decoded_digits = [morse_to_digit.get(char, '?') for char in morse_chars]

# 将解析结果连接为字符串
decoded_string = ''.join(decoded_digits)

# 输出结果
print(decoded_string)