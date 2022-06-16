# My most complex project yet! This took me days to finish.
# Something I wished to add is the automatic tile clearing which reduces tediousness and boredom...
# ...but I was not skilled enough to come up and implement that concept.
import random

# Buffering things
grid = []
xGrid = []
newGrid = []
gridCoverOld = []
gridCover = []
gridCoverX = []
bombCounter = 0
bombExploded = False
unknownCounter = 0
x = 9
y = 9
debug = True

bombs = 10
blanks = x * y - bombs

for bomb in range(0, bombs):  # Grid generator
    grid.append("*")
for blank in range(0, blanks):
    grid.append("&")
random.shuffle(grid)  # Generates bombs and blanks and shuffles to create a list, soon to be 2d list.

for yAxis in range(0, y):  # Grid organiser
    for xAxis in range(0, x):
        xGrid.append(grid[x * yAxis:x * yAxis + x])
    newGrid.append(xGrid[yAxis])
    xGrid.clear()

for yCover in range(0, x * y):  # Grid cover generator (cover the mines duh)
    gridCoverOld.append("?")
for yAxis in range(0, y):
    for xAxis in range(0, x):
        gridCoverX.append(gridCoverOld[x * yAxis:x * yAxis + x])
    gridCover.append(gridCoverX[yAxis])

for yCoord in range(0, y):  # Find the indexes of & in the grid (THANKS PAUL FROM GDT!!!)
    #  Searches for every combination of coordinates to find &
    for xCoord in range(0, x):
        if newGrid[yCoord][xCoord] == "&":
            for adjacentYSpaces in range(0, y):  # my doing... I learned this pattern and manage to use it to find bombs.
                for adjacentXSpaces in range(0, x):
                    if newGrid[adjacentYSpaces][adjacentXSpaces] == "*":
                        # Checking all adjacent sides for bombs then applying numbers for their tiles.
                        # 8 if statements work but for loops doesn't when checking adjacent sides.
                        # This is bc when it reaches the max range it stops but increase the max by 1 is out of index range.
                        if adjacentYSpaces == yCoord - 1 and adjacentXSpaces == xCoord - 1:
                            bombCounter = bombCounter + 1
                        if adjacentYSpaces == yCoord - 1 and adjacentXSpaces == xCoord:
                            bombCounter = bombCounter + 1
                        if adjacentYSpaces == yCoord - 1 and adjacentXSpaces == xCoord + 1:
                            bombCounter = bombCounter + 1
                        if adjacentYSpaces == yCoord and adjacentXSpaces == xCoord - 1:
                            bombCounter = bombCounter + 1
                        if adjacentYSpaces == yCoord and adjacentXSpaces == xCoord + 1:
                            bombCounter = bombCounter + 1
                        if adjacentYSpaces == yCoord + 1 and adjacentXSpaces == xCoord - 1:
                            bombCounter = bombCounter + 1
                        if adjacentYSpaces == yCoord + 1 and adjacentXSpaces == xCoord:
                            bombCounter = bombCounter + 1
                        if adjacentYSpaces == yCoord + 1 and adjacentXSpaces == xCoord + 1:
                            bombCounter = bombCounter + 1
            newGrid[yCoord].insert(xCoord, bombCounter)
            newGrid[yCoord].pop(xCoord + 1)
            bombCounter = 0

# Credit: https://stackoverflow.com/questions/47582312/how-to-print-a-2d-list-so-that-each-list-is-on-a-new-line-with-a-space-without
if debug:  # Debug purpose; prints the solution
    for row in newGrid:
        for col in row:
            print(col, end=" ")  # print each element separated by space
        print()  # Add newline
    print()

while not bombExploded:  # Same thing but prints the grid cover every turn (for playing)
    for row in gridCover:
        for col in row:
            print(col, end=" ")  # print each element separated by space
        print()  # Add newline
    # Player inputs xCoords and yCoords to mine
    mineX = input("Choose the X-coordinate you wish to mine [(1,1) is top left, (9,9) is bottom right.]: ")
    try:  # Checks if the input is valid (only allows int!)
        int(mineX)
    except:
        print("This does not work!")
        break
    if 0 < int(mineX) < 10:
        mineY = input("Choose the Y-coordinate you wish to mine [(1,1) is top left, (9,9) is bottom right.]: ")
        try:
            0 < int(mineY) < 10
        except:
            print("This does not work!")
            bombExploded = True
            break
        if 0 < int(mineY) < 10:  # Grid is 9x9!
            gridCover[int(mineY)-1].insert(int(mineX)-1, newGrid[int(mineY)-1][int(mineX)-1])
            gridCover[int(mineY)-1].pop(int(mineX))  # Mines a certain area
            if newGrid[int(mineY)-1][int(mineX)-1] == "*":  # Mined a bomb, game over
                for exposingBombY in range(0, y):
                    for exposingBombX in range(0, x):
                        if newGrid[exposingBombY][exposingBombX] == "*":
                            gridCover[exposingBombY].insert(exposingBombX, newGrid[exposingBombY][exposingBombX])
                            gridCover[exposingBombY].pop(exposingBombX + 1)
                for row in gridCover:  # When a bomb is mined, a screen shows all bombs and later game over.
                    for col in row:
                        print(col, end=" ")
                    print()
                print("You mined a bomb! GAME OVER!")
                break
            if newGrid[int(mineY)-1][int(mineX)-1] == 0:  # My best attempt to reduce tediousness in game
                for adjacentClearY in range(0, y):
                    # Same code for checking adjacent sides, but it mines these sides instead
                    for adjacentClearX in range(0, x):
                        if adjacentClearY == int(mineY)-2 and adjacentClearX == int(mineX)-2:
                            gridCover[int(mineY) - 2].insert(int(mineX) - 2, newGrid[int(mineY) - 2][int(mineX) - 2])
                            gridCover[int(mineY) - 2].pop(int(mineX)-1)
                        if adjacentClearY == int(mineY)-2 and adjacentClearX == int(mineX)-1:
                            gridCover[int(mineY) - 2].insert(int(mineX) - 1, newGrid[int(mineY) - 2][int(mineX) - 1])
                            gridCover[int(mineY) - 2].pop(int(mineX))
                        if adjacentClearY == int(mineY)-2 and adjacentClearX == int(mineX):
                            gridCover[int(mineY) - 2].insert(int(mineX), newGrid[int(mineY) - 2][int(mineX)])
                            gridCover[int(mineY) - 2].pop(int(mineX)+1)
                        if adjacentClearY == int(mineY)-1 and adjacentClearX == int(mineX)-2:
                            gridCover[int(mineY) - 1].insert(int(mineX) - 2, newGrid[int(mineY) - 1][int(mineX) - 2])
                            gridCover[int(mineY) - 1].pop(int(mineX)-1)
                        if adjacentClearY == int(mineY)-1 and adjacentClearX == int(mineX):
                            gridCover[int(mineY) - 1].insert(int(mineX), newGrid[int(mineY) - 1][int(mineX)])
                            gridCover[int(mineY) - 1].pop(int(mineX)+1)
                        if adjacentClearY == int(mineY) and adjacentClearX == int(mineX)-2:
                            gridCover[int(mineY)].insert(int(mineX) - 2, newGrid[int(mineY)][int(mineX) - 2])
                            gridCover[int(mineY)].pop(int(mineX)-1)
                        if adjacentClearY == int(mineY) and adjacentClearX == int(mineX)-1:
                            gridCover[int(mineY)].insert(int(mineX) - 1, newGrid[int(mineY)][int(mineX) - 1])
                            gridCover[int(mineY)].pop(int(mineX))
                        if adjacentClearY == int(mineY) and adjacentClearX == int(mineX):
                            gridCover[int(mineY)].insert(int(mineX), newGrid[int(mineY)][int(mineX)])
                            gridCover[int(mineY)].pop(int(mineX)+1)
            for scanningY in range(0, y):  # Checks for any available clear tiles.
                for scanningX in range(0, x):
                    if gridCover[scanningY][scanningX] == "?":
                        unknownCounter = unknownCounter + 1
            if unknownCounter == bombs:  # When all tiles can be cleared, it's a win!
                print("All areas are cleared! YOU WIN")
                break
            unknownCounter = 0
        else:
            print("That number is out of range!")
    else:
        print("That number is out of range!")
