with open('test.txt', 'r') as f:
    print("The file is opened in mode: " + f.mode)
    pass

f2 = open("test.txt", 'r')
print("The file f2 is: " + f2.name)

#print(f.mode)
