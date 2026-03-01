from motor import motor 
from sensors import Dustsensor ,ultrasonicSensor
from vehicle import vehicle



class CleaningSystem :

    def __init__(self):
        self.vehicle = vehicle()
        self.vacuum_motor = motor("Vacuum")
        self.broom_motor = motor("Broom")
        self.dust_sensor = Dustsensor() 
        self.ultra_sensor = ultrasonicSensor()


    def start_cleaning(self):
        print("--- Starting Cleaning System ---")  


        #step 1 :cheak obstacle 
        distance = self.ultra_sensor.detect_obstacle()


        if distance <20:
            self.vehicle.stop()
            print("obstacle detected ! cannot move forward.")
            return
          
        # step 2: move forward
        self.vehicle.move_forward()


        #step 2 : check dust level 
        dust = self.dust_sensor.detect_dust()

        if dust >50 :
            print("High dust level detected! Starting vacuum motor.")
            self.vacuum_motor.start()
            self.broom_motor.start()
        else :
            print("Dust level is low. No need to start cleaning.")


        print("--- Cleaning System Operation Completed ---")    