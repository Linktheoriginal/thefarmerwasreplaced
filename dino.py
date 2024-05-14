def dinoMode():
	clear()
	fillEggs()
	
def putEggAndMove():
	buyNeededItem(Items.Egg)
	use_item(Items.Egg)
	moveNext()
	
def fillEggs():
	putEggAndMove()
	while not home():
		putEggAndMove()
	sortField(dino_tuning)
	harvestAll()
	