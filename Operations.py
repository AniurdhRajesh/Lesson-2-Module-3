
mixed_tuple = (5, "Hello", 3.14, True, None)
print("Mixed Tuple:", mixed_tuple)

int_tuple = (1, 2, 3, 4, 5, 2)
print("Integer Tuple:", int_tuple)
added_tuple = tuple(x + 9 for x in int_tuple)
print("New Tuple after adding 9:", added_tuple)
element_to_count = 2
count = int_tuple.count(element_to_count)
print(f"The element {element_to_count} occurs {count} times in the integer tuple.")
sliced_tuple = int_tuple[:3]
print("Sliced Tuple (first 3 elements):", sliced_tuple)
sliced_tuple_end = int_tuple[-3:]
print("Sliced Tuple (last 3 elements):", sliced_tuple_end)
