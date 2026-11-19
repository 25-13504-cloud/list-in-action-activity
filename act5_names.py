names = []

for i in range(5):
    name = input("Enter name: ")
    names.append(name)

reversed_names = names[::-1]
sorted_names = sorted(names)

print("Original Names:", names)
print("Reversed Names:", reversed_names)
print("Sorted Names:", sorted_names)
