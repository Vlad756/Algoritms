arr1 = ['a', 'b', 'c', 'x']
arr2 = ['z', 'y', 'c']

def func(ar1, ar2):
	for i in arr1:
		for j in arr2:
			if i == j:
				return print(True)
	return print(False)

def containsCommonItem(ar1, ar2):
	mapp = {}
	for i in range(len(ar1)):
		if ar1[i] not in mapp.keys():
			item = ar1[i]
			mapp.update({item: True})

	for j in range(len(arr2)):
		if ar2[j] in mapp.keys():
			return print(True)
	return print(False)

func(arr1, arr2) # O(a*b)
containsCommonItem(arr1, arr2) # O(a+b)

#any_in = lambda arr1, arr2: any(i in arr2 for i in arr1)

#any_in2 = lambda arr1, arr2: bool(set(arr1).intersection(arr2))

any_in = any(i in arr2 for i in arr1)
any_in2 = bool(set(arr1).intersection(arr2))
print(any_in)
print(any_in2)