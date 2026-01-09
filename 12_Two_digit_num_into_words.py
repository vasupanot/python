#Hello

no=input('Enter a two digit number:') #input always returns a string
no=int(no)
print('number is :',no)

first=no//10
last=no%10

print('first is :',first)
print('last is :',last)

list=['zero','one','two','three','four','five','six','seven','eight','nine']
print(list[first],' ',list[last])
