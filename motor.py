class motor:

    #we make sttribute name becouse we have three moters
    def __init__(self , name):
       self.name = name
       self.status = "OFF"

    def start(self) :
        self.status = "ON"
        print(f"{self.name} moter is motor started.")

    def stop(self) :
        self.status = "OFF"
        print(f"{self.name}  moter is motor stopped.")

