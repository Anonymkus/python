import timeit

def insertion_sort(nums0: list) -> list:
	counter = 1
	for i in range(1, len(nums0)):
		for j in range(i, 0, -1):
			# print("========================")
			# print(f"spisok: {nums0}")
			if nums0[j] < nums0[j - 1]:
				nums0[j], nums0[j - 1] = nums0[j - 1], nums0[j]
				# print(f"menayem {nums0[j]} i {nums0[j - 1]}")
				# print(f"popytka {counter}")
				counter += 1
			else:
				# print(f"popytka {counter}")
				counter += 1
				break
	return nums0


nums0 = [i for i in range(100)]
nums0.reverse()


def test_insertion_sort():
	global nums0
	insertion_sort(nums0)

print(nums0)
print(sorted(nums0))
print(insertion_sort(nums0))
print(timeit.timeit(test_insertion_sort, number=100))

# ==================================================================================
print("==========================================================================")

def quick_sort(nums1: list) -> list:
	if len(nums1) > 1:
		barrier = nums1[0]
		small = [i for i in nums1 if i < barrier]
		big = [i for i in nums1 if i > barrier]
		equal = [i for i in nums1 if i == barrier]
		nums1 = quick_sort(small) + equal + quick_sort(big)
	return nums1

nums1 = [i for i in range(100)]
nums1.reverse()


def test_quick_sort():
	global nums1
	quick_sort(nums1)

print(nums1)
print(sorted(nums1))
print(quick_sort(nums1))
print(timeit.timeit(test_quick_sort, number=100))
