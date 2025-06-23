FizzBuzz = []
for i in range(3):
    a = input()
    if a.isdigit():
        FizzBuzz.append(int(a))
        b = i
    else:
        FizzBuzz.append(a)
c = FizzBuzz[b] + 3 - b
st = ''
if c % 3 == 0:
    st += 'Fizz'
if c % 5 == 0:
    st += 'Buzz'
if st == '':
    print(c)
else:
    print(st)