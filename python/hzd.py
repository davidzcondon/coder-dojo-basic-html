from collections import namedtuple

def print_family():
  family = input("How many people are in your family?\n>> ")
  for num_people in range(int(family)):
    name = input("What is your name?\n>> ")
    age = input("How old are you?\n>> ")
    print("Hello " + name + "!!! You are " + str(age) + " years old.")

def print_hzd():
  favourite_machine = input("What is your favourite machine?\n>> ")
  print("You like " + favourite_machine + " but I like Metal Devils")

Machine = namedtuple('Machine', 'name, strength, weakness')

def print_faro_machines():
  metal_devil = Machine("Metal Devil", "Corruption", "Nothing")
  deathbringer = Machine("Deathbringer", "Corruption", "Fire")
  corruptor = Machine("Corruptor", "Corruption", "Fire")

  faro_machine_list = [metal_devil, deathbringer, corruptor]
  for machine in faro_machine_list:
    print(machine.name + " is a Faro Machine"
      + ". It is strong against " + machine.strength
      + ". It is weak against " + machine.weakness + ".")

def print_datapoints():
  datapoints = ["Hologram", "Audio", "Reading"]
  print("There are " + str(len(datapoints)) + " types of datapoints.")

  for datapoint in datapoints:
    print("There are " + datapoint + " datapoints.")

choice = input("What do you want me to do?\n A) Print Faro Machines\n B) Print Datapoints\n C) Print Favourite Machine\nEnter A or B or C >> ")

if (choice is "A"):
  print_faro_machines()
elif (choice is "B"):
  print_datapoints()
elif (choice is "C"):
  print_hzd()
else:
  print("You didn't enter A or B!!!")