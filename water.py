def water():
	if get_water() < .75:
		if num_items(Items.Water_Tank) == 0:
			trade(Items.Empty_Tank)
		use_item(Items.Water_Tank)