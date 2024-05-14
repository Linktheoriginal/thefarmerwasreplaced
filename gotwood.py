def plantWoodField():
	clear()
	plantWood()
	moveNext()
	while not home():
		harvest() #free hay
		water()
		plantWood()
		moveNext()

def plantWood():
	if shouldPlantTree():
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
		
def shouldPlantTree():
	if get_pos_x() % 2 == 0:
		return get_pos_y() % 2 == 0
	else:
		return get_pos_y() % 2 == 1