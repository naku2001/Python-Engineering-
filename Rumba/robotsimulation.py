MaxX = 9
MaxY = 9
x,y = 0,0
dockX,dockY = 0,0

dirtX, dirtY = 5,6
print("Starting roomba at ", x ,y)
dirtFound = False
while (y < MaxY and dirtFound ==False):
    while (x < MaxX):
        x += 1
        print("Moved to" ,x ,y)
        if (x == dirtX and y == dirtY):
            if not dirtFound:
                print("Dirt Collected at ", x, y)
            dirtFound = True
            break
    y += 1
    print("Moved to" ,x ,y)
    if (dirtFound==True or (x == dirtX and y == dirtY)):
        print("Dirt Collected at ", x, y)
        break

    while (x > 0):
        x -= 1
        print("Moved to" ,x ,y)
        if (x == dirtX and y == dirtY):
            if not dirtFound:
                print("Dirt Collected at ", x, y)
            dirtFound = True
            break

while (x > 0):
    x -= 1
    print("Moved to" ,x ,y)
    while (y > 0):
        y -= 1
        print("Moved to" ,x ,y)
print("RETURNED HOME")