class Car:
<<<<<<< HEAD
    #20200607 vss 
=======
>>>>>>> 8c313ca99d4b666506d1d9fa3d86f16eb1b2981e
    def __init__(self):
        self.speed = 0
        self.odometer = 0
        self.time = 0
<<<<<<< HEAD

=======
'''20200607'''
>>>>>>> 8c313ca99d4b666506d1d9fa3d86f16eb1b2981e
    def say_state(self):
        print("I am going {}kph!".format(self.speed))

    def acceleter(self):
        self.speed+= 5

    def brake(self):
        self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1
<<<<<<< HEAD
        

        
=======
>>>>>>> 8c313ca99d4b666506d1d9fa3d86f16eb1b2981e

    def average_speed(self):
        if self.time == 0:
           print("self.time = 0")
        return self.odometer / self.time

if __name__ == '__main__':
    my_car = Car()
    print("I am a car!")
    while True:
        action = input("What should I do? [A]ccelerate,[B]rake,"
                       "show [O]dometer,or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) !=1:
            print("I dont know how to do that")
            continue
        if action == 'A':
            my_car.acceleter()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()
        print("20190616 修改")
        print("20190717xiuga")
        print("20190617xiugai")
        print("20190618")

<<<<<<< HEAD
        print("in branch dev")
        print("in branch 20190622")
<<<<<<< HEAD
        print("in master 20190622")
=======
        print("in branch 20190622")
        

>>>>>>> feature1

=======
>>>>>>> 8c313ca99d4b666506d1d9fa3d86f16eb1b2981e




