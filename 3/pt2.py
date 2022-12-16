X = [l.strip() for l in open('input.txt')]
total = 0


def sort_string(s):
    output = []
    for char in line:
        if (char.isupper()):
            number = ord(char)-38
        else:
            number = ord(char)-96
        output.append(number)
    return sorted(output)


def score(c):
    if 'a' <= c <= 'z':
        return ord(c)-ord('a') + 1
    else:
        return ord(c)-ord('A') + 1 + 26


i = 1
chars = []
for line in X:
    chars.append(line)
    if i % 3 == 0:
        x, y, z = list(chars[0]), list(chars[1]), list(chars[2])
        for c in x:
            if c in y:
                if c in z:
                    total += score(c)
                    break
        chars = []
    i += 1

print(total)
