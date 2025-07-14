f= open ('zaid.txt','r')

# print (f.read())

# now create a new text file?

f1= open ('abc','w')
for data in f:
    f1.write(data)