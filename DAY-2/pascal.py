def pascal_triangle(n):
    for line in range(n):
        print(" " * (n - line), end="")
        val = 1
        for i in range(line + 1):
            print(val, end=" ")
            val = val * (line - i) // (i + 1)
        print()

rows = int(input("Enter number of rows: "))
pascal_triangle(rows)
