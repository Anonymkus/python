import collections
def count_item():
	with open('items.txt', 'r', encoding='utf-8') as file:
		items_list = file.read().splitlines()
	counter_a = collections.Counter()
	for w in items_list:
		counter_a[w] += 1

	item_dict = dict(counter_a)
	
	for key,values in item_dict.items():
		print(key, ":", values, "|", values * 100 / len(items_list), "%")

count_item() 
