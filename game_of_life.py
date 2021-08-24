# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
# These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

# Any live cell with two or three live neighbours survives.
# Any dead cell with three live neighbours becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

# inputList = [[1,0,1,1,1],[0,1,1,1,1]]
# neigh = [0]*len(input[0])
# bottom_neigh = neigh[:]
# top_neigh = neigh[:]
###
#(0,neighs) 0 0 0 0 
#1 0 1 1 1
#0 1 1 1 1
#{
#    (0,0) : 
#}

#}
### neigh for r,c = (r+1,c), (r+1,c+1), (r-1,c)
def play(width,height,liveCells):
    cells = [[0]*width for _ in range(height)]
    for row,column in liveCells:
        cells[row][column] = 1
    neigh = [0]*width
    cells.append(neigh[:])
    cells = [neigh] + cells
    del neigh
    for row,column in liveCells:
        if column-1 >=0:
            cells[row][column-1] += 1 #left
        if column+1 <width:
            cells[row][column+1] += 1 #right
        cells[row-1][column] += 1     #top
        cells[row+1][column] += 1     #bottom
        cells[row+1][column+1]+=1     #right lower diagonal
        cells[row+1][column-1]+=1     #left lower diagonal
        cells[row-1][column-1]+=1     # 
        
width = 5
height = 2
liveCells = {(0,1),(0,3),(0,4),(0,2),(1,1),(1,2),(1,3),(1,4)}
play(width,height,liveCells)
