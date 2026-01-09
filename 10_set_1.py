#Hello

# create set and operation on set
names ={'Rahul','Rohan','manish','Rajesh','Mohit'}

#print Set
print(names)

#add new item
names.add('Jitesh')
print("\nSet after add ",names)

#update item
names.update(["Yash","Ketan","Tushar"])
print('\nset after update :',names)

#remove
names.remove('Rahul')
print('\nSet after remove :',names)

#try to add duplicate item
names.add('Yash')
print('\nSet after add duplicate record :',names)


a ={1,2,3,4,5}
b ={3,4,5,6,7}

#union
print('\nUnion : ',a.union(b))

#intersaction
print("\nIntersaction : ",a.intersection(b))

#difference
print("\nDifference :",a.difference(b))  # a-b
