nums = [n for n in range(20)] 
nums2 = [2, 4, 6, 2]

# List
even = [n for n in nums if n%2==0]
print(even)

# Sets
binary = {n**2 for n in nums2}
print(binary)

# nested
twoDArray = [[1,2], [3,4], [5,6]]
spreadedArray = [num for x in twoDArray for num in x]
print(spreadedArray)

# Generator
generator = (num**num for num in nums2)
print(next(generator))
print(next(generator))