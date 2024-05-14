def tillif():
	if get_ground_type() == Grounds.Turf:
			till()

def untill():
	if get_ground_type() == Grounds.Soil:
			till()
			
def buyNeededItem(item):
	if num_items(item) == 0:
		trade(item, trade_batch)