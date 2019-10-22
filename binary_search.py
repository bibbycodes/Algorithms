import math

# returns index of item being searched for
def binary_search(array, search_item):
  low = 0
  high = len(array) - 1
  iteration = 0

  while low <= high:
    mid = math.floor((low + high) / 2)
    guess = array[mid]

    if guess == search_item:
      print("Found item at index {}, it took {} iterations".format(mid, iteration))
      return mid
      
    if guess < search_item:
      low = mid + 1
    else:
      high = mid - 1
    
    iteration += 1
  
  print("Item not in list")
  return None

input = [1,2,3,4,5,6,7,8,9,10]
    
print(binary_search(input, 10))