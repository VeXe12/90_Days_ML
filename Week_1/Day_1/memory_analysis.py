import sys
print("--- Experiment 1: Mutability ---")

# 1. Create a list and print its memory address (ID)
my_list = [1-3]
add_list_before = id(my_list)
print(f'List ID before append: {add_list_before}')

# 2. Append to the list and check ID again
my_list.append(4)
add_list_after = id(my_list)
print(f'List ID after append: {add_list_after}')

if add_list_before == add_list_after:
    print('List is MUTABLE cause address not changed\n')
else:
    print('List is IMMUTABLE cause address changed\n')

# 3. Repeat for Tuple
my_tuple = (1, 2, 3)
add_tuple_before = id(my_tuple)
print(f'Tuple ID before append: {add_tuple_before}')

# Tuples don't have .append(), so we must concatenate (creating a new object)
my_tuple += (4,)
add_tuple_after = id(my_tuple)
print(f'Tuple ID after append: {add_tuple_after}')

if add_tuple_before == add_tuple_after:
    print('Tuple is MUTABLE cause address not changed\n')
else:
    print('Tuple is IMMUTABLE cause address changed\n')


import array
print("--- Experiment 2: Memory Overhead ---")

# Create sequences with 1 million integers
N = 1_000_000

# A standard Python List (Stores pointers to Integer Objects)
list_obj = list(range(N))

# A Python Tuple (Stores pointers, but fixed size structure)
tuple_obj = tuple(range(N))

# A Compact Array (Stores raw C-integers, no overhead pointers)
# 'i' stands for signed integer (4 bytes usually)
array_obj = array.array('i', range(N))

print(f'List size: {sys.getsizeof(list_obj) / 1024 / 1024:.2f} MB')
print(f'Tuple size: {sys.getsizeof(tuple_obj) / 1024 / 1024:.2f} MB')
print(f'Array size: {sys.getsizeof(array_obj) / 1024 / 1024:.2f} MB\n')

print("NOTE: The List is larger because it is a Dynamic Array that over-allocates to allow growth.\n")

