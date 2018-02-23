
'''
Created on 2017年9月19日

@author: Saya
'''
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) +
     "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

def describe_pet( pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

         
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
         print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over!")