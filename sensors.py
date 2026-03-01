import random
   

class Dustsensor :
    

    def __init__(self ):
        self.dust_level = 0

    def detect_dust(self):
        # randum generated simulate dust value
        self.dust_level = random.randint(0, 100)
        print(f"Dust level detected: {self.dust_level} ")
        return self.dust_level
    


class ultrasonicSensor :
    

    def __init__(self ):
        self.distance = 0


    def detect_obstacle(self):
        # random generated simulate distance between 5cm to 100cm    
        self.distance = random.randint(5,100)
        print(f"distance detected :{self.distance} cm")
        return self.distance