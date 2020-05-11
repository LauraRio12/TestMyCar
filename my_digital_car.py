#class definition
class Car:
    name=""
    brand=""
    color=""
    speed= 0

    def __init__(self,name,brand,color,speed):
        self.name= name
        self.brand= brand
        self.color= color
        self.speed=speed

    def the_speed(self):
            print(self.name +" is driving at "+ str(self.speed)+ " km/h")

    def the_brand(self):
            print(self.name + " brand is "+ self.brand )

    def the_color(self):
            print(self.name+ " color is "+ self.color)
#object

priscilla= Car("Priscilla", "Porshe","red", 200)
priscilla.the_speed()
priscilla.the_brand()
priscilla.the_color()



