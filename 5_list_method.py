
places =['Ahmedabad','Bhavnagar','Surat','Jamnagar','Bhavnagar','Rajkot','Bhavnagar']
 
print(places)
 #insert new Item in First Position
places.insert(0,'Dwarka')
print(places)
 
 #insert new Item in Last Position
places.append('Gandhinagar')
print(places)
 
 #Find Index number of given Item
print(places.index('Surat'))

#find out how many times places repeat
print(places.count('Bhavnagar'))
 
 #Remove Item from list 
places.remove('Jamnagar')
print(places)

#Remove item from given index
places.pop(0)
print(places)
 
 #copy one list into another 
places2=places.copy()
print(places2)
 
 #Remove all items from list
places2.clear()
print(places2)

print('Good bye')