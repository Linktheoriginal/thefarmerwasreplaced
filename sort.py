def sortField(passes):
	moveTo(0, 0)
	bubbleSort(passes)

def bubbleSort(passes):
	passNum = 0
	sorted = False
	passSorted = True
	while not sorted and passNum < passes:
		if not bubbleSwap():
			passSorted = False
		moveNext()
		if home():
			passNum = passNum + 1
			if passSorted:
				sorted = True
			else:
				passSorted = True			

def bubbleSwap():
	sorted = True
	this = measure()
	
	that = measure(East)
	if (this > that and get_pos_x() < farm_size - 1):
		swap(East)
		sorted = False

	that = measure(North)
	if (this > that and get_pos_y() < farm_size - 1):
		swap(North)
		sorted = False

	return sorted