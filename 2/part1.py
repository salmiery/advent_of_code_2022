X = [l.strip() for l in open('input.txt')]


# AX    = ROCK     = 1
# BY    = PAPER    = 2
# CZ    = SCIS     = 3
total = 0


def pointcheck(move):
    match move:
        case "A" | "X":
            return 1
        case "B" | "Y":
            return 2
        case "C" | "Z":
            return 3


def winCheck(num, me):
    match num:
        case "op":
            return me
        case "dr":
            return 3 + me
        case "me":
            return 6 + me


def convert(num):
    match num:
        case 1:
            return "Rock"
        case 2:
            return "Paper"
        case 3:
            return "Scisors"


for f in X:
    op, me = f.split()
    op = pointcheck(op)
    me = pointcheck(me)
    winner = ""
    if op == 1:
        if me == 3:
            winner = "op"
    if me == 1:
        if op == 3:
            winner = "me"

    if winner == "":
        if me > op:
            if me == 3 & op == 1:
                winner = "op"
            else:
                winner = "me"
        elif me == op:
            winner = "dr"
        else:
            winner = "op"

    pts = winCheck(winner, me)
    total += pts
    print("OP: " + convert(op) + "\tME: " + convert(me) +
          "\tRes: " + winner + "\t\tPts: " + str(pts))

print("----------"*6)
print("Total:\t" + str(total))
