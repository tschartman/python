
def printMatrix(Matrix):
    for col in range(len(Matrix)):
        for row in range(len(Matrix[col])):
            print(Matrix[col][row], ' ', end='')
        print('')

def fillCol(Matrix, row_index):
    for col in range(len(Matrix)):
        for row in range(len(Matrix[col])):
            if col == row_index:
                Matrix[col][row] = 1

def fillRow(Matrix, col_index):
    for col in range(len(Matrix)):
        for row in range(len(Matrix[col])):
            if row == col_index:
                Matrix[col][row] = 1

def fillRowPerm(Matrix, amount, spaces):
    for col in range(len(Matrix)):
        # if 1's in row = amount then set 0's to ' '
        for row in range(len(Matrix[col])):
            print()

# Todo: integrate lists to keep track of amount filled in in each colum/row

def countFill(Matrix, colCount, rowCount):
    for col in range(len(Matrix)):
        for row in range(len(Matrix[col])):
            if Matrix[col][row] == 1:
                colCount[row] += 1
                rowCount[col] += 1


def fill_matrix(Matrix, rows, num_rows, cols, num_cols):
    assert (len(rows) == num_rows), "Rows list not equal to # of rows"
    assert (len(cols) == num_cols), "Cols list not equal to # of columns"
    rowCount = [0 for x in range(num_rows)]
    colCount = [0 for x in range(num_cols)]

    for index, valSet in enumerate(rows):
        value = valSet.split(',')[0]
        if len(valSet.split(',')) > 1:
            space = valSet.split(',')[1]
        else:
            space = 0
        assert (int(value) <= num_cols), "Amount of filled greater than size of row"
        if int(value) == num_rows:
            fillCol(Matrix, index)
        else:
            fillRowPerm(Matrix, value, space)
    for index, valSet in enumerate(cols):
        value = valSet.split(',')[0]
        assert (int(value) <= num_cols), "Amount of filled greater than size of col"
        if int(value) == num_cols:
            fillRow(Matrix, index)
    countFill(Matrix, colCount, rowCount)
    print("Rows: ", rowCount)
    print("Cols: ", colCount)



try:
    num_rows = int(input("# of Rows: "))
    num_cols = int(input("# of Columns: "))
    rows = input("Rows: ")[1:-1].split('","')
    cols = input("columns: ")[1:-1].split('","')
except ValueError:
    raise SystemExit("Input given was not a valid number")

Matrix = [[0 for x in range(num_cols)] for y in range(num_rows)] 
fill_matrix(Matrix, rows, num_rows, cols, num_cols)
printMatrix(Matrix)