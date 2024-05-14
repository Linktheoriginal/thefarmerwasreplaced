def treasureMode():
	if get_entity_type() == Entities.Hedge:
		solveMaze(North)

	if get_entity_type() == Entities.Grass:
		plant(Entities.Bush)
	elif get_entity_type() == Entities.Bush:
		if num_items(Items.Fertilizer) == 0:
			trade(Items.Fertilizer, trade_batch)		
		use_item(Items.Fertilizer)
	else:
		clear()

def solveMaze(direction):
	if get_entity_type() == Entities.Treasure:
		harvest()
		return
	else:
		direction = rightHandRuleMove(direction)
	solveMaze(direction)

def rightHandRuleMove(direction):
	if move(right[direction]):
		return right[direction]
	elif move(direction):
		return direction
	else:
		return left[direction]
