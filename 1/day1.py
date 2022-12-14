f = open("input.txt", "r")

leader = 0
current = 0

for x in (f.readlines()):
    if x == "\n":
        if current > leader:
            leader = current
        current = 0
    else:
        current += int(x)

print(leader)
