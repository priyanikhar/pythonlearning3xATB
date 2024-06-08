#List- shopping List
#milk,bread, butter,poha
#1.Add item
#2.Remove item
#3.Update item
#4.View item
#5.Exit

shopping_list=["milk","bread","butter","poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[1])
# Adding item to list # append add item basically at the end
shopping_list.append("coffee")
print(shopping_list)

# Insert ,add item at the middle or in between of ist
shopping_list.insert(3,"Brownie")
print(shopping_list)

# Extend add multiple item in the end
shopping_list.extend(["chocolate","oats","fruits","Almand"])
print(shopping_list)
shopping_list.extend(["kiwi"])
print(shopping_list)#['milk', 'bread', 'butter', 'Brownie', 'poha', 'coffee', 'chocolate', 'oats', 'fruits', 'Almand', 'kiwi']

# pop remove last item from the list
shopping_list.pop()
print(shopping_list)# ['milk', 'bread', 'butter', 'Brownie', 'poha', 'coffee', 'chocolate', 'oats', 'fruits', 'Almand']


#Reverse

shopping_list.reverse()
print(shopping_list)

#Sorting


my_list=[1,2,3,4,True,3.14,"Pramod"]
print(type(my_list)) # <class 'list'>