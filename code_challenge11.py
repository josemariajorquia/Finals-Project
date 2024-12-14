for x in range(5, 0, -1): 
	for u in range(1, x+1):
		print(" ", end=" " )
	for v in range(5, x, -1):
		print("*", end= " ")
	for y in range(4, x, -1):
		print("*", end= " ")
	print()

for z in range(0,5):
	for u in range(1, z+1):
		print(" ", end= " " )
	for v in range(5, z, -1):
		print("*", end= " ")
	for y in range(4, z, -1):
		print("*", end= " ")
	print()