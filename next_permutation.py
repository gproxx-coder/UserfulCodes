def next_bigger(num):
	# Check whether number is in descending order OR same digit or single digit
	# If yes then retuen -1
	if len(set(str(num))) == 1 or int("".join(sorted(list(str(num)), reverse=True))) == num:
		return -1

	right_greater_idx,mid_point = 0,0

	# Find middle point to split the number
	chars = list(str(num))
	for idx in range(len(chars)-1,-1,-1):
		if not chars[idx] <= chars[idx-1]:
			mid_point = idx
			break

	# keeping left and right parts seperately and also middle value
	mid_char = [chars[mid_point-1]]
	left = chars[:mid_point-1]
	right = chars[mid_point:]
	right = sorted(right)
	for idx in range(len(right)):
		if right[idx] > mid_char[0]:
			right_greater_idx = idx
			break

	# Swapping the middle point with next greater number from right part
	mid_char[0], right[right_greater_idx] = right[right_greater_idx], mid_char[0]

	return int("".join(left) + mid_char[0] + "".join(right))
	
print(next_bigger(99642))


# One more solution
def next_bigger(n):
    if str(n) == ''.join(sorted(str(n))[::-1]):
        return -1
    a = n
    while True:
        a += 1
        if sorted(str(a)) == sorted(str(n)):
            return a

print(next_bigger(144))
