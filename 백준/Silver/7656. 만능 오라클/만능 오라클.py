input_data = input()
sentences = []
current = ""
for char in input_data:
    current += char
    if char in ['.', '?']:
        sentences.append(current.strip())
        current = ""
for sentence in sentences:
    if sentence.startswith("What is") and sentence.endswith("?"):
        answer = "Forty-two" + sentence[4:-1] + "."
        print(answer)