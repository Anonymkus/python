import random

num = random.randint(0, 101)
nums = [i for i in range(random.randint(1, 11), random.randint(11, 101))]
nums.sort()

print(f"список {nums}")
print(f"число {num}")

start_idx = 0
stop_idx = len(nums) - 1

while start_idx <= stop_idx:
	mid_idx = (start_idx + stop_idx) // 2
	mid_num = nums[mid_idx]

	if mid_num == num:
		print(f"{num} найден на индексе {mid_idx}")
		break
	elif num > mid_num:
		start_idx = mid_idx + 1
	elif num < mid_num:
		stop_idx = mid_idx - 1
else: 
	print(f"числа {num} не оказалось в списке")
