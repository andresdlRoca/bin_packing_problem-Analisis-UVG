def bin_packing(items, bin_capacity):
    items = [item[0] for item in items]  # Extract the integers from the tuples
    items.sort(reverse=True)  # Sort the items in descending order of size

    bins = []  # List to store the bins

    for item in items:
        # Check if the item fits in any existing bin
        for bin in bins:
            if item <= bin_capacity - sum(bin):  # Check if there is enough capacity in the bin
                bin.append(item)  # Add the item to the bin
                break
        else:
            # Create a new bin if the item does not fit in any existing bin
            bins.append([item])

    return bins




# if __name__ == "__main__":
#   # Create a list of items.
#   items = [(10, "Item 1"), (15, "Item 2"), (20, "Item 3"), (25, "Item 4"), (30, "Item 5")]

#   # Set the bin capacity.
#   bin_capacity = 30

#   # Solve the bin packing problem.
#   bins = bin_packing(items, bin_capacity)

#   # Print the number of bins used.
#   print("Bins used:", len(bins))

#   # Print the contents of each bin.
#   print("\nContent of bins:")
#   for bin in bins:
#     print(bin)
