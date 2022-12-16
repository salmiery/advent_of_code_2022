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


for line in X:
    chars = list(line.strip())
    half = len(chars)//2

    x = chars[:half]
    y = chars[half:]
    for c in x:
        if c in y:
            total += score(c)
            break


print("Total: " + str(total))
