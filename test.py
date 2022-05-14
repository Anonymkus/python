import random

nums = [i for i in range(10)]
nums.reverse()
# random.shuffle(nums)
counter = 1

print(nums)

for i in range(len(nums)):
	for num_id in range(len(nums) - 1 - i):
		print(f"spisok do   : {nums}")
		if nums[num_id] > nums[num_id + 1]:
			nums[num_id], nums[num_id + 1] = nums[num_id + 1], nums[num_id]
			print(f"pomenyalis: {nums[num_id]} i {nums[num_id + 1]}")
		print(f"spisok posle: {nums}, popytka {counter}")
		print("--------------------------------------------")
		counter += 1

print(nums)
