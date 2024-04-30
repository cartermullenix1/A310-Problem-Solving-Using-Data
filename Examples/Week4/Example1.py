# t = {}
# t["nick"] = "truther"
# t["nolan"] = "truther"
# t[(3,4)] = 9
# t[(2,1)] = 1
# print(t)


size = 5

m = {}
m["width"] = size
m["height"] = size

def show(m):
    for row in range(m["height"]):
        for col in range (m["width"]):
            if (row, col) in m:
                print(m[row,col], end = " ")
            else:
                print(0, end = " ")
        print()

# show(m)
row = size - 1
col = size//2
for n in range(1,size*size+1):
    m[row, col] = n
    newrow = (row + 1) % size
    newcol = (col + 1) % size
    if (newrow, newcol) in m:
        row = row - 1
        col = col
    else:
        row = newrow
        col = newcol

show(m)