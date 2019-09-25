import math


def binary_search(list, item):
  low = 0
  high = len(list) - 1
  loop = 0

  while low <= high:
    loop += 1
    mid = (low + high) // 2
    guess = list[mid]
    if guess == item:
      return loop
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None


x = int(input("Określ wielkość zbioru\n"))
y = int(input("Wskaż szukaną liczbę\n"))
my_list = [x for x in range(x + 1)]
print("Sukces po ilości prób: ", binary_search(my_list, y))


print("O (log n) wynosi:", int(math.log(x, 2)))
