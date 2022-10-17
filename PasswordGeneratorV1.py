#PasswordGeneratorV1
import random as rand
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Capsalphabet = ["A","B","C","D","E","F","G","H","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = [0,1,2,3,4,5,6,7,8,9]
password = ""
pass_length = 8
x = 0 
while x <= pass_length:
  randletter = rand.randint(0,25)
  whatlist = rand.randint(0,2)
  randnum = rand.randint(0,9)
  if whatlist == 0:
    password = password + alphabet[randletter]
  elif whatlist == 1:
    password = password + Capsalphabet[randletter]
  elif whatlist == 2:
    password = password + str(numbers[randnum])
  x += 1
print (password)