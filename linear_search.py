def linear_search(array, target):
  for i in range(len(array)):
    if array[i] == target:
      return i
    
  return -1
  

data = [2,5,9,1,6]
target = 8

result = linear_search(data, target)
print(result)

if result != -1:
  print("The element is at index", result)
else:
  print("The element was not found!")