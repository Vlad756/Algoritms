# def firstRecurringCharacter(inputt):
# 	for i in inputt:
# 		for j in inputt[1:]:
# 			if i == j:
# 				return i
# 	return False
# print(firstRecurringCharacter([2,1,1,2,3,5,1,2,4]))

# def firstRecurringCharacter2(inputt):
# 	i = 0
# 	while i < len(inputt):
# 		j = 1
# 		while j < len(inputt):
# 			if inputt[i] == inputt[j]:
# 				return inputt[i]
# 			j += 1
# 		i += 1
# 	return False

def firstRecurringCharacter(inputt): # time O(n^2), space O(1)
	for i in range(0, len(inputt)):
		for j in range(i+1, len(inputt)):
			if inputt[i] == inputt[j]:
				return inputt[i]
	return False

def firstRecurringCharacter2(inputt): # O(n)
	hash_map = {}
	for i in range(len(inputt)):
		if inputt[i] in hash_map:
			print(hash_map)
			return inputt[i]
		else:
			hash_map[inputt[i]] = i
	return False

print(firstRecurringCharacter([2,5,5,2,3,5,1,2,4]))
