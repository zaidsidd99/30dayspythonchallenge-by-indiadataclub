# #LIST____

# food = ['burger','pizza','samosa','pasta','cold_coffee']
# print(len(food))

# ##############################################################

# food = ['burger','pizza','samosa','pasta','cold_coffee']
# print (food[0:4])

# ################################################################

# food = ['burger','pizza','samosa','pasta','cold_coffee']

# food.insert(0,'noodles')
# print (food)

# ################################################################

# food = ['burger','pizza','samosa','pasta','cold_coffee']
# num= [6,4,3,1,5,2]
# num.sort ()
# print (num)

# ######################################################################

# food = ['burger','pizza','samosa','pasta','cold_coffee']

# food_str=('-'.join(food))
# print (food_str)


##############################################################################33

# Create an inventory system tracking items and quantities with a dictionary ?

food = {"burger":40,"pizza":10, "fries":40,"momos":10}

#item quantity__
print("burger available:",food["burger"])

#add item___
food["pasta"] = 5

#update item__
food["burger"]+= 5

# remove item__
del food["momos"]

# display full food stock____
for item,quantity in food.items():
    print(item,"-",quantity)
