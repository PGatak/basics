from collections import deque

kolejka = deque([])
kolejka.append(1)
kolejka.append(2)
kolejka.append(3)
kolejka.append(4)
print(kolejka)
kolejka.popleft()
print(kolejka)

# mozna takze uzyc listy i pop(0)


