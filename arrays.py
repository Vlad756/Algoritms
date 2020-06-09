strings = ['a', 'b', 'c', 'd']
#4*4 = 16 bytes of storage

print(strings[2]) #O(1)

#append
strings.append('e') #O(1) or O(n)

#pop
strings.pop() #O(1)

#insert
strings.insert(0,'x') #O(n)

print(strings)