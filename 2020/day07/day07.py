import re 

test_input = [
	"light red bags contain 1 bright white bag, 2 muted yellow bags.",
	"dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
	"bright white bags contain 1 shiny gold bag.",
	"muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
	"shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
	"dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
	"vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
	"faded blue bags contain no other bags.",
	"dotted black bags contain no other bags.",
]

MY_BAG = "shiny gold"

class Bag:
	def __init__(self, color, bags, bags_qty):
		self.color = color
		self.bags = bags
		self.bags_qty = bags_qty

def check_sub_bags(all_bags, bag_color, current_bags):
	if bag_color == "no other":
		return current_bags
	else:
		for bag in all_bags:
			if bag_color in bag.bags:
				current_bags.append(bag.color)
				check_sub_bags(all_bags, bag.color, current_bags)
		return current_bags

def create_bags(bags):
	all_bags = []
	for bag in bags:
		[ color, contains ] = bag.split(" bags contain ")
		contains_list = contains.split(", ")
		bags_qty_list = [bag.replace(" bags", "").replace(" bag", "").strip(".") for bag in contains_list]
		bags_no_qty_list = [re.sub('\d ', '', bag) for bag in bags_qty_list]
		all_bags.append(Bag(color, bags_no_qty_list, bags_qty_list))
	return all_bags

def count_containing_bags(all_bags):
	current_bags = []
	for bag in all_bags:
		for containing_bag in bag.bags:
			if containing_bag == MY_BAG:
				current_bags.append(bag.color)
				current_bags = check_sub_bags(all_bags, bag.color, current_bags)
	return len(set(current_bags))

if __name__ == "__main__":
	with open('input.txt', 'r') as f:
		rules = [line.strip() for line in f]
	
	all_test_bags = create_bags(test_input)
	all_bags = create_bags(rules)
	
	print(count_containing_bags(all_test_bags))
	print(count_containing_bags(all_bags))