def rotate(nums, k):  # O(n)
    array = nums
    for i in range(k-1):
        lastI = array[-1]
        print(lastI)
        array.insert(0, lastI)
        array.pop(-1)
    print(array)

# leftRotatebyOne([1,2,3,4,5,6,7], 3)


for i in range(10, 0, -1):
    print(i)
