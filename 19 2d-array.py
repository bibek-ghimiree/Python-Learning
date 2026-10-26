matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])       # First row
print(matrix[1][2])    # 6

# Print all elements
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

matrix[0][0] = 100
print(matrix)