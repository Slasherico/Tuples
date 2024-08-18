#Example of a tuple
colors = ('red', 'green', 'blue')
print(colors)
print(colors[1])

#-Packing-
#(When you group items together in a tuple, 
#it’s called packing.)
address = ('Square_24', 'Villa_19', 'House_num_...')
for item in address: #below (end = '') is the space in between each item
    print(item, end = ' ')

#-Unpacking-
#(You can also take items out of a tuple
#and assign them to variables. This is called unpacking.)
Area, HouseNam, HouseNo = address
print('A',Area)

#Tuple without these -> () <-
my_tuple = 'Oore', 14, 'Canada'
print(my_tuple)

xtra = ('extra', 'amount',[1,2,3])
print(xtra[2][1])