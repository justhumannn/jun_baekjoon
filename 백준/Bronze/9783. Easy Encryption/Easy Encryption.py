import sys

input_str = sys.stdin.read().rstrip('\n')
result = []
for char in input_str:
    if 'a' <= char <= 'z':
        code = ord(char) - ord('a') + 1
        result.append(f"{code:02d}")
    elif 'A' <= char <= 'Z':
        code = ord(char) - ord('A') + 27
        result.append(f"{code:02d}")
    elif '0' <= char <= '9':
        result.append(f"#{char}")
    else:
        result.append(char)
print("".join(result))