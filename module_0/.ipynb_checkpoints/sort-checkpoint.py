def bubble_sort_names(names):
    # Get the number of elements in the list
    n = len(names)
    # Perform Bubble Sort
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if names[j] > names[j+1]:
                names[j], names[j+1] = names[j+1], names[j]
    return names

# Example usage
names_list = ["Anna", "John", "Peter", "Maria", "Zoe"]
sorted_names = bubble_sort_names(names_list)

print("Names sorted alphabetically without using .sort():")
for name in sorted_names:
    print(name)
