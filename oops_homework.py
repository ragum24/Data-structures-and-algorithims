class Capy:  
#init is a constructor function to create the properties :) 
    def __init__(self,name,weight,food,colour,height,conservation_status,cuteness_level):
        self.name=name
        self.weight=weight
        self.food=food
        self.colour=colour
        self.height=height
        self.conservation_status=conservation_status
        self.cuteness_level=cuteness_level

    def details(self):
        print(f"This capybara's name is {self.name}")
        print(f"The average weight of {self.name} is {self.weight} kg")
        print(f"{self.name} eat {self.food}")
        print(f"{self.name}'s main colours are {self.colour}")
        print(f"The average height of {self.name} is {self.height} cm")
        print(f"The level of concern for capybaras is {self.conservation_status}")
        print(f"The cuteness of a {self.name} out of 10 is {self.cuteness_level}")


Cap=Capy("Brownie",66,"grass, grains, fruits and reeds.","brown and dark brown.",62,"least concern.","100+/10. Way too cute and calm!!!")
Cap.details()