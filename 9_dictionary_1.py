#Hello

#example of dictionary 2
book = {}
print(book)
book['name'] = 'C language'
book['author'] = 'Paresh Rathod'
book['price'] = 180
print(book)

#add tuple into dictionary
book['chapters'] = (1,2,3,4,5)
book['topic'] = ['Array','Loop','Pointer','String']
print(book)

#display only 1st Topic and last topic
print(book['topic'][0])
print(book['topic'][3])

#Add topic into list of dictionary 
book ['topic'] = 'conclusion of array'
print(book)