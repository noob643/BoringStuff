tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
        colWidths = [0]*len(data)
    
    for i in range(len(data)):
        width = 0
        for j in data[i]:
            if len(j) > width:
                width = len(j)
        colWidths[i] = width
        
    for y in range(len(data[0])):
        for z in range(len(data)):
            print(data[z][y].rjust(colWidths[z]), end = ' ')
        print()
    
printTable(tableData)
