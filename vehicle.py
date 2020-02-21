class Vehicle
    def __init__(self,make,model,year,weight,trips,NeedsMaintenance):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.trips = trips
        self.maintenance = NeedsMaintenance

    def TripsSinceMaintenance(self):
        if self.trips > 100:
            NeedsMaintenance = False
        else:
            NeedsMaintenance = True


    def NeedsMaintenance(self):
        if self.maintenance = False
            return("Vehicle is good to go!")
        else:
            return("Vehicle needs repair!")
            self.trips = 0


class Cars(Vehicle)
    def __init__(self,make,model,year,weight,trips,NeedsMaintenance,DrivingStatus):
        Vehicle.__init__(self,make,model,year,weight,trips,NeedsMaintenance):
        self.DrivingStatus = DrivingStatus

    def IsDriving(self,True):
        if self.DrivingStatus = "Drive":
            return("Going on a trip")
        if self.DrivingStatus = "Stop":
            return("End of trip")
            trips += 1

    
