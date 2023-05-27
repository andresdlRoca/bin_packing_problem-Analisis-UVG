def bin_packing(items, bin_capacity):
  """
  Solves the bin packing problem using the greedy algorithm.

  Args:
    items: A list of items, where each item is a tuple of (size, name).
    bin_capacity: The capacity of each bin.

  Returns:
    A list of bins, where each bin is a list of items.
  """

  # Sort the items in decreasing order of size.
  items.sort(key=lambda x: x[0], reverse=True)

  # Create a list to store the bins.
  bins = []

  # Start with the first item and place it in the first bin.
  current_bin = []
  current_bin.append(items[0])

  # For each subsequent item, try to place it in the current bin.
  # If it fits, then place it in the current bin.
  # Otherwise, create a new bin and place the item in the new bin.
  for item in items[1:]:
    if item[0] <= bin_capacity - current_bin[0][0]:
      current_bin.append(item)
    else:
      bins.append(current_bin)
      current_bin = []
      current_bin.append(item)

  # Add the last bin to the list of bins.
  bins.append(current_bin)

  return bins


if __name__ == "__main__":
  # Create a list of items.
  items = [(10, "Item 1"), (15, "Item 2"), (20, "Item 3"), (25, "Item 4"), (30, "Item 5")]

  # Set the bin capacity.
  bin_capacity = 30

  # Solve the bin packing problem.
  bins = bin_packing(items, bin_capacity)

  # Print the number of bins used.
  print("Bins used:", len(bins))

  # Print the contents of each bin.
  print("\nContent of bins:")
  for bin in bins:
    print(bin)
