def cc13():

for x in range (1,6):
	for u in range (6,x, -1) :
		print(" ", end= " ")
	for v in range(x,1,-1) :
		print(v, end = " ")
	for y in range (1, x+1):
		print(y, end= " ")
	print()
for z in range (4,0,-1):
	for u in range(6,z, -1):
		print(" ", end= " ")
	for v in range(z, 1,-1):
		print(v, end= " ")
	for y in range (1,z+1):
		print(y, end= " ")
	print()

cc13():
