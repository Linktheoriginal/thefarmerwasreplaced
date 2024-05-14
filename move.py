def moveNext():
	move(North)
	if get_pos_y() == 0:
		move(East)
def home():
	return get_pos_x() == 0 and get_pos_y() == 0
def moveTo(x, y):
	while x < get_pos_x():
		move(East)
	while x > get_pos_x():
		move(West)
	while y < get_pos_y():
		move(South)
	while y > get_pos_y():
		move(North)