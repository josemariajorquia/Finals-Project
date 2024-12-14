for x in range(6,0, -1) :
	for u in range (1,x+1):
		print(" ", end= "")
	for v in range (5,x, -1) :
		print("*", end= "")
	for y in range (5,x, -1):
		print("*", end= "")
	print()
for z in range(4,0, -1):
	for u in range (1,5-2):
		print(" ", end= " ")
	for v in range (6,z, -5):
		print ("*", end= "") 
	for y in range (6,z, -5):
		print ("*", end= "")
	print()