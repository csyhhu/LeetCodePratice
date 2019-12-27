def largestRectangleArea(heights):
	"""
	Time Limit Exceeded
	"""
	area = []
	for idx, h in enumerate(heights):
		count = 1

		cur_idx = idx - 1
		while (cur_idx >= 0):
			if heights[cur_idx] >= h:
				count += 1
			else:
				break
			cur_idx -= 1
		
		cur_idx = idx + 1
		while (cur_idx < len(heights)):
			if heights[cur_idx] >= h:
				count += 1
			else:
				break
			cur_idx += 1
		area.append(h * count)

	# print(area)
	return max(area)


def largestRectangleArea2(heights):
	if len(heights) == 0:
            return 0
	heights.append(-1)
	stack = []
	max_area = -1
	for idx, h in enumerate(heights):
		# print(stack)
		# if len(stack) > 0:
		# 	print(idx, heights[stack[-1]], h)
		if len(stack) == 0 or (len(stack) > 0 and heights[stack[-1]] <= h):
			# print(stack)
			stack.append(idx)
		else:
			# Pop all the heights that is larger than h
			while (len(stack) > 0 and heights[stack[-1]] >= h):
				pop_idx = stack.pop(0)
				# Area
				# print (idx, pop_idx, heights[pop_idx])
				leftArea = (pop_idx + 1  if len(stack) == 0 else pop_idx - stack[-1]) * heights[pop_idx]
				rightArea = (idx - pop_idx - 1) * heights[pop_idx]
				# print (rightArea)
				if (rightArea + leftArea) > max_area:
					max_area = rightArea
			# Push h
			stack.append(idx)
		print(stack)
	return max_area


def largestRectangleArea3(heights):
	if len(heights) == 0:
            return 0
	heights.append(0)
	stack = []
	max_area = -1
	for idx, h in enumerate(heights):
		while(len(stack) != 0 and heights[stack[-1]] > h):
			pop_idx = stack.pop()
			leftArea = (pop_idx + 1  if len(stack) == 0 else (pop_idx - stack[-1])) * heights[pop_idx]
			rightArea = (idx - pop_idx - 1) * heights[pop_idx]
			# print (rightArea)
			if (rightArea + leftArea) > max_area:
				max_area = rightArea
		stack.append(idx)
	return max_area


def largestRectangleArea4(heights):
	"""
	Codes copied from: https://www.cnblogs.com/boring09/p/4231906.html
	"""
	if len(heights) == 0:
            return 0
	heights.append(0)
	stack = []
	max_area = -1

	for idx, h in enumerate(heights):
		if (len(stack) == 0 or heights[stack[-1]] < h):
			stack.append(idx)
		else:
			while (len(stack) > 0 and h <= heights[stack[-1]]):
				right_boundary = heights[stack[-1]]
				stack.pop()
				w = idx if len(stack) == 0 else idx - stack[-1] - 1
				max_area = max(max_area, w * right_boundary)
			stack.append(idx)
	return max_area

# inputs =  [2,1,5,6,2,3]
# inputs = [4, 2]
# inputs = [0,0]
inputs = [2,1,2]
print(largestRectangleArea4(inputs))