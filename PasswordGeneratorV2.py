#PasswordGeneratorV2
import random as rand
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
capsalphabet = ["A","B","C","D","E","F","G","H","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = [0,1,2,3,4,5,6,7,8,9]
specialcharacters = ["!","@","#","$","%","^","&","*","(",")","_","-","+","=","<",">",",",".","?","/",";",":","~","`","{","}","[","]","|"]
password = ""
pass_length = 8
x = 0 

#function
def passmaker(specchar):
  global alphabet
  global capsalphabet
  global numbers
  global specialcharacters
  global password
  global pass_length
  global x
  while x <= pass_length:
    randletter = rand.randint(0,25)
    if specchar == "y":
      whatlist = rand.randint(0,3)
    else:
      whatlist = rand.randint(0,2)
    randnum = rand.randint(0,9)
    randchar = rand.randint(0,29)
    if whatlist == 0:
      password = password + alphabet[randletter]
    elif whatlist == 1:
      password = password + capsalphabet[randletter]
    elif whatlist == 2:
      password = password + str(numbers[randnum])
    elif whatlist == 3:
      password = password + (specialcharacters[randchar])
    x += 1
  print(password)
#events
speccharyn = input("Would you like to include special characters? y or n ")
passmaker(speccharyn)