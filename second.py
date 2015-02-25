from first import fill_tetrahedron

def tetrahedron_filled(tetrahedrons, water):
	tetrahedrons.sort()

	filled=0
	
	for element in tetrahedrons:
		currentElementVolume = fill_tetrahedron(element)
		water = water - currentElementVolume
		
		if water > 0:
			filled = filled + 1
		else:
			break

	return filled

