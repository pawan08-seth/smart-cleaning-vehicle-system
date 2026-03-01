class vehicle :
    def __init__(self):
        self.is_moving = False


    def move_forward(self) :
        self.is_moving = True
        print("Vehicle is moving forward.")

    def stop(self) :
        self.is_moving = False
        print("Vehicle has stopped.")

    def turn_left(self) :
        print("Vehicle is turning left.")

    def turn_right(self) :
        print("Vehicle is turning right.")               
