def print_table(table):
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(len(max(table[j], key=len)) + 1), end='')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)
