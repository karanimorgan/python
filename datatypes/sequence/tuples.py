empty = ()
# print(empty)

fruits = ("Apples", "banana", "cherry")
# print(fruits)
# print(fruits[1])

# specialtuples
items = (1,2,3,[10, 20, 30, 40], "john","james", ["Mango", "Cherry"])
print(items[3][2])

# immutability of tuples
list_items = [1, 2, 3, 4, 5]
# items = (1, 2, 3, 4, 5)
# items[3] = 10
# list_items[3] = 10
print(list_items) #This will print the modified list
# print (items) this will raise typr error because tuples are immutable

items = (1,2,3,[10, 20, 30, 40], "john","james", ["Mango", "Cherry"])
items[3][2] = 100
print(items)



