print("Tuple operations\n")
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
print("First element:", my_tuple[0])
print("Slice [1:4]:", my_tuple[1:4])
print("Length:", len(my_tuple))
print("Count of 3:", my_tuple.count(3))
print("Index of 4:", my_tuple.index(4))

print("\nDictionary operations\n")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nDictionary:", my_dict)
print("Keys:", list(my_dict.keys()))
print("Values:", list(my_dict.values()))
print("Items:", list(my_dict.items()))
my_dict['d'] = 4
print("After adding 'd':", my_dict)
my_dict.pop('b')
print("After removing 'b':", my_dict)
print("Get 'c':", my_dict.get('c'))

print("\nSet operations\n")
my_set = {1, 2, 3, 4}
another_set = {3, 4, 5, 6}
print("\nSet:", my_set)
my_set.add(5)
print("After adding 5:", my_set)
my_set.remove(2)
print("After removing 2:", my_set)
print("Union:", my_set.union(another_set))
print("Intersection:", my_set.intersection(another_set))
print("Difference:", my_set.difference(another_set))