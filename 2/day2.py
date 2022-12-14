f = open("input.txt", "r")

leader = 0
current = 0
array = []
total = 0

# Creating a bubble sort function


def bubbleSort(list1):
    # Outer loop for traverse the entire list
    for i in range(0, len(list1)-1):
        for j in range(len(list1)-1):
            if (list1[j] > list1[j+1]):
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1


# Read the file
for x in (f.readlines()):
    if x == "\n":
        array.append(current)
        current = 0
    else:
        current += int(x)

# Sort it
sortedArray = bubbleSort(array)

# Sum it
for i in sortedArray[-3:]:
    total += i
# Print it
print(total)
