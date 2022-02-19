def show_squares(width, height):
	if width > height:
		max_value = height
	elif width < height:
		max_value = width
	else:
		max_value = height

	area_tetragon = width * height

	for i in range(1, (max_value + 1)):
		if area_tetragon % (i ** 2) == 0 and max_value % i == 0:
			print(i, area_tetragon // (i ** 2))
		else:
			pass


show_squares(1080, 1920)
