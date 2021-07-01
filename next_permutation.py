def next_bigger(num):
	right_greater_idx,mid_point = 0,0
	# Find middle point
	chars = list(str(num))
	for idx in range(len(chars)-1,-1,-1):
		if not chars[idx] <= chars[idx-1]:
			mid_point = idx
			break

	mid_char = [chars[mid_point-1]]
	left = chars[:mid_point-1]
	right = chars[mid_point:]
	right = sorted(right)
	for idx in range(len(right)):
		if right[idx] > mid_char[0]:
			right_greater_idx = idx
			break

	mid_char[0], right[right_greater_idx] = right[right_greater_idx], mid_char[0]

	op = int("".join(left) + mid_char[0] + "".join(right))
	if op == num:
		return -1
	else:
		return op

print(next_bigger(1234567980 ))

def findnext(ii):
    iis=list(map(int,str(ii)))
    for i in reversed(range(len(iis))):
        if i == 0: return ii
        if iis[i] > iis[i-1] :
            break        
    left,right=iis[:i],iis[i:]
    for k in reversed(range(len(right))):
        if right[k]>left[-1]:
           right[k],left[-1]=left[-1],right[k]
           break
    return int("".join(map(str,(left+sorted(right)))))


print(findnext(1234567980 ))
