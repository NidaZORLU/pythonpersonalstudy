class Araba:
    def __init__(self, speed, color):  #init serves as a constructor. this is the first method that will be called when you create an instance
        #print(speed)  #self means "the current object"
        #print(color)
        self.speed = speed
        self.color = color

    def set_speed(self, value):
        self.speed= value

    def get_speed(self):
        return self.speed

ford = Araba(200,'red') # Ford is and object of the class Araba
sahin = Araba(220,'blue')
tofas = Araba(250,'black')

tofas.set_speed(110)
print(tofas.get_speed())
print(tofas.color)

tofas.speed=210
print(tofas.speed)