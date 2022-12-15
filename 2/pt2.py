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


def opcheck(op, me):
    # print("OP: " + convert(pointcheck(op)) + "\tME: " + me)
    op = pointcheck(op)
    match me:
        case "X":
            if op == 1:
                return 3
            return op - 1
        case "Y":
            return op + 3
        case "Z":
            if op == 3:
                return 7
            if op == 2:
                return 9
            if op == 1:
                return 8


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
    pts = opcheck(op, me)
    if pts == 0:
        print("WOMP WOMP")
    # print("Points: "+str(pts))
    total += pts
print("----------"*6)
print("Total:\t" + str(total))
