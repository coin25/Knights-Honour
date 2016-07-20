#Austin Young
#Custom Made Encryption, this file is just for reference
#January 22, 2016

#This is the highscore
number = 48

#Squaring the highscore
number = number*number
#Making a list for the encryption
number_list = []
#Making the list full of the number
for i in range(number):
    number_list.append(i)
#Creating the character list
characters = []
#Encrypts
for i in number_list:
    #Multiplies the number by 4
    n = i*4
    #Takes the integer then roots it
    n = int(n**0.5)
    #Takes the proper chr value and appends it to the list
    x = chr(n+40)
    #Adds them to characters
    characters.append(x)

print(characters)
print(len(characters))

#To get around anyone editing anything in the file, all this does to unencrypt is check the length of the list.
#Hacking the highscore is very difficult now, especially not knowing this.
print(len(characters)**0.5)




