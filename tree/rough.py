


arr = [1, -3, -3, 6, 8]

seen = set()
totals_dict = {}
total = 0

ans = []

for i, val in enumerate(arr):
    # everytime, add new total to totals_dict as a key
    # and value would be i (index itself)
    total += arr[i]
    # If prefix sum is 0 or it is already present meaning, we got the ans
    if total == 0 or total in seen:
        ans = [totals_dict[total], i]
    seen.add(total)
    totals_dict[total] = i

print(ans)
