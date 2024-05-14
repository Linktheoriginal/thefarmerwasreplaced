mode = 1
automode = True
base = 10000
min_hay = 7 * base
min_wood = 6 * base
min_carrot = 5 * base
min_pumpkin = 4 * base
min_gold = 3 * base
min_cactus = 2 * base
min_power = 2 * base

mode_change_threshold = 10000
max_wood = min_wood + mode_change_threshold
max_carrot = min_carrot + mode_change_threshold
max_pumpkin = min_pumpkin + mode_change_threshold
max_gold = min_gold + mode_change_threshold
max_cactus = min_cactus + mode_change_threshold

trade_batch = 10
farm_size = 1
dino_tuning = 8

plantSeedMap = {
	Entities.Carrots: Items.Carrot_Seed,
	Entities.Cactus: Items.Cactus_Seed,
	Entities.Pumpkin: Items.Pumpkin_Seed,
	Entities.Sunflower: Items.Sunflower_Seed,
}

right = {
	North: East,
	East: South,
	South: West,
	West: North,
}

left = {
	North: West,
	West: South,
	South: East,
	East: North,
}

while True:
	if mode == 1:
		harvestMode()
	elif mode == 2:
		treasureMode()
	elif mode == 3:
		dinoMode()
	if automode:
		mode = switchMode(mode)

def switchMode(mode):
	if home() and mode == 1:
		if num_items(Items.Cactus) > max_cactus:
			return 3
		if num_items(Items.Gold) < min_gold and num_items(Items.Pumpkin) > min_pumpkin:
			return 2
	elif mode == 2:
		if num_items(Items.Cactus) > max_cactus:
			return 3
		if num_items(Items.Pumpkin) < min_pumpkin or num_items(Items.Gold) > max_gold:
			return 1
	elif mode == 3:
		if num_items(Items.Cactus) < min_cactus:
			return 1
	return mode