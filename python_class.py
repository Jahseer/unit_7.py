class Sundae:
	def __init__(self, icecream, sauce, topping):
		self.icecream = icecream
		self.sauce = sauce
		self.topping = topping

	
order1 = Sundae('strawberry', 'chocolate', 'cherries', 'peanuts')
print(f'{order1}')