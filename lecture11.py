
#Input a poem file
poem_file = open('poem11.txt', encoding='utf-8')
content = poem_file.read()

#Change letters in capital letters 
print(content.upper())

#Add one boolean flag parameter
x = 'content.upper'
if x is content.lower:
    print(True)
else:
    print(False)

poem_file.close()



