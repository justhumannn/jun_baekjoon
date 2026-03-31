import sys

parsed_lines = []
max_len = []

while True:
    line = sys.stdin.readline()
    if not line:
        break
        
    words = line.split()
    if not words:
        continue
        
    parsed_lines.append(words)
    
    for i in range(len(words)):
        if i >= len(max_len):
            max_len.append(len(words[i]))
        else:
            if len(words[i]) > max_len[i]:
                max_len[i] = len(words[i])

for words in parsed_lines:
    res = ""
    for i in range(len(words)):
        if i == len(words) - 1:
            res += words[i]
        else:
            res += words[i].ljust(max_len[i]) + " "
    print(res)