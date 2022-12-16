correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]


# Define a function check_sudoku() here:
def check_sudoku2(sodoku):
    expected_values = list(range(1, len(sodoku) + 1))
    print(expected_values)


# Define a function check_sudoku() here:
def check_sudoku(sodoku):
    column_verified_values = []
    for column_index in range(len(sodoku)):
        row_verified_values = []
        for row in sodoku:
            if row[column_index] not in column_verified_values:
                column_verified_values.append(row[column_index])
            else:
                return False

            for value in row:
                if isinstance(value, int) is False or value in row_verified_values:
                    return False
                else:
                    row_verified_values.append(value)
            row_verified_values = []
        column_verified_values = []
    return True


print(check_sudoku2(correct))

print(check_sudoku(incorrect))
# >>> False

print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False
