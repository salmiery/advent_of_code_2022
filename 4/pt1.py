# X = [l.strip() for l in open('control.txt')]

X = [l.strip() for l in open('input.txt')]
count = 0

for line in X:
    x, y = line.split(",")
    x1, x2 = x.split("-")
    y1, y2 = y.split("-")

    if (int(x1) <= int(y1) and int(x2) >= int(y2)) or (int(y1) <= int(x1) and int(y2) >= int(x2)):
        count += 1

print(count)
