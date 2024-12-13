for x in range(6,0, -1):
    for u in range (1,x+1):
        print(" " , end= " ")
    for v in range(6,x, -1):
        print("*", end = " ")
    for y in range(6,x, -1):
        print("*", end = " ")
    print()
    
for z in range(1,6):
    for u in range(1,z+1):
        print(" " , end=" ")
    for v in range(6,z, -1):
        print("*", end = " ")
    for y in range (6,z,-1):
        print("*", end = " ")
    print()