import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Provided Solution (runtime: 15.133995771408081 seconds)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# List Comprehension solutiom (runtime: 3.1780054569244385 seconds)
# duplicates = [name_1 for name_1 in names_1 if name_1 in names_2]

# O(n)? solution (runtime: 3.527998208999634 seconds)
# duplicates = []
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

# "Optimized" Solution 1: runtime: 88.04000115394592 seconds, 0.1049964427947998 seconds to make the tree.
# bst_2 = BinarySearchTree(names_2[0]) 
# for i in range(1,len(names_2)):
#     bst_2.insert(names_2[i])
# end_time_1 = time.time()
# print (f'{time.time() - start_time} seconds to make the tree.')
# duplicates = []
# for name in names_1:
#     if bst_2.contains(name):
#         duplicates.append(name)

# Optimized solution 2: runtime: 0.012006998062133789 seconds
duplicates = []
name_1_set = set(names_1)
name_2_set = set(names_2)
for name in name_1_set.intersection(name_2_set):
    duplicates.append(name)

end_time = time.time()
duration = end_time - start_time
time_provided = 15.133995771408081
multiple = round(time_provided/duration,1)
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {duration} seconds")
print(f'Optimized solution runs {multiple} times faster than the provided solution ')
print()
