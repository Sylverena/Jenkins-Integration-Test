# This program finds the syracuse sequence for a given integer, then prints it to console.

def syracuse(x):    # uses a re
    if x == 1:
        syracuseList.append(int(x))
        return x
    if x % 2 == 0:
        syracuseList.append(int(x))
        return syracuse(x / 2)
    else:
        syracuseList.append(int(x))
        return syracuse(3 * x + 1)


syracuseList = []
seed = input("Enter number to print syracuse for > ")
syracuse(int(seed))

print(syracuseList)
