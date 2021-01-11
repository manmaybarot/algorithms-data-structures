# Quick Sort

from random import randint


def quick_sort(left, right, A):
	if left >= right:
		return
	pivot_index = randint(left, right)
	pivot_index = partition(left, right, pivot_index, A)

	is_left_part_small = pivot_index - left < right - pivot_index
	if is_left_part_small:
		quick_sort(left, pivot_index-1, A)
		quick_sort(pivot_index + 1, right, A)
	else:
		quick_sort(pivot_index + 1, right, A)
		quick_sort(left, pivot_index-1, A)


def partition(left, right, pivot_index, A):
	pivot_ele = A[pivot_index]
	A[right], A[pivot_index] = A[pivot_index], A[right]

	store_index = left
	for i in range(left, right):
		if A[i] < pivot_ele:
			if i != store_index:
				A[i], A[store_index] = A[store_index], A[i]
			store_index += 1

	A[right], A[store_index] = A[store_index], A[right]

	return store_index



if __name__ == '__main__':
    A = [14,3,5,67,85,4,32,4,67,55,66,55]
    quick_sort(0, len(A)-1, A)
    print(A)


# worst case for space complexity happens when algorithms runs
# for average time complexity.
# e.g: every time pivot will be the middle and our call stack will
# store at most log(N) items.
