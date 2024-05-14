def harvestMode():
	if can_harvest():
		harvest()
	if num_items(Items.Hay) < min_hay:
		untill()
	elif num_items(Items.Wood) < min_wood:
		plantWoodField()
		harvestAll()
	elif num_items(Items.Carrot) < min_carrot:
		plantFullField(Entities.Carrots)
		harvestAll()
	elif num_items(Items.Pumpkin) < min_pumpkin:
		plantFullField(Entities.Pumpkin)
		harvest()
	elif num_items(Items.Power) < min_power:
		plantFullField(Entities.Sunflower)
		harvestLargest()
	else:
		plantFullField(Entities.Cactus)
		sortField(100)
		harvest()

def plantTilledEntity(entity):	
	buyNeededItem(plantSeedMap[entity])
	tillif()
	return plant(entity)

def harvestAll():
	moveTo(0, 0)
	while not can_harvest():
		#wait for wood
		do_a_flip()
	harvest()
	moveNext()
	while not home():
		harvest()
		moveNext()

#special multi pass planting code for pumpkins
def plantPumpkinPatch():
	clear()
	fullField = False
	fullPass = False
	while not fullField:
		if home():
			if fullPass == True:
				fullField = True
			fullPass = True
		if plantTilledEntity(Entities.Pumpkin):
			fullPass = False
		moveNext()

def plantFullField(entity):
	if entity == Entities.Pumpkin:
		plantPumpkinPatch()
		return
	clear()
	plantTilledEntity(entity)
	moveNext()
	while not home():
		harvest() #free hay
		water()
		plantTilledEntity(entity)
		moveNext()
		
def harvestLargest():
	moveTo(0, 0)
	biggestValue = measure()
	smallestValue = measure()
	locationX = 0
	locationY = 0
	moveNext()
	
	while not home():
		if measure() > biggestValue:
			biggestValue = measure()
		if measure() < smallestValue:
			smallestValue = measure()
		moveNext()
	
	for size in range(biggestValue, smallestValue - 1, -1):
		if measure() == size:
			harvest()
		moveNext()
		
		while not home():
			if measure() == size:
				harvest()
			moveNext()	
	