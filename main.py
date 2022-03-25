from random import choice

def rand_num(num):
  num = choice(range(1,7))
  return num
  
user = ""
while user != "Y":
  user = input ("Do ou want to roll the dice?")

while user == "Y":
  num = 0
  num = rand_num(num)
  #dice face
  
  
  if num == 1:
    print (" ----------")
    print ("|         |")
    print ("|    0    |")
    print ("|         |")
    print (" ----------")
  
  if num == 2:
    print (" ----------")
    print ("|      0  |")
    print ("|         |")
    print ("|  0      |")
    print (" ----------")
  
  if num == 3:
    print (" ----------")
    print ("|       0 |")
    print ("|    0    |")
    print ("|  0      |")
    print (" ----------")
  
  if num == 4:
    print (" ----------")
    print ("|  0   0  |")
    print ("|         |")
    print ("|  0   0  |")
    print (" ----------")
  
  if num == 5:
    print (" ----------")
    print ("|  0   0  |")
    print ("|    0    |")
    print ("|  0   0  |")
    print (" ----------")
  
  if num == 6:
    print (" ----------")
    print ("|  0    0 |")
    print ("|  0    0 |")
    print ("|  0    0 |")
    print (" ----------")
  user = input("do you want to roll again? Y or N")