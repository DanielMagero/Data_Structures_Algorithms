def linear_search_modified(array, target):
  indices = []

  for i in range(len(array)):
    if array[i] == target:
      indices.append(i)

  return indices

array = [1,4,3,6,7,4,4,5,4,6,7,3,4,6,8,9,5,9]
target = 4

result = linear_search_modified(array, target)

if result:
  print("Elements found at indices", result)
else:
  print("Element not found!")