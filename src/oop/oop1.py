# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

##### BASE CLASS #####
class Vehicle():
    pass

##### PARENT #####
class FlightVehicle(Vehicle):
    pass

##### CHILD #####
class Starship(FlightVehicle):
    pass

##### CHILD #####
class Airplane(FlightVehicle):
    pass

##### PARENT #####
class GroundVehicle(Vehicle):
    pass

##### CHILD #####
class Car(GroundVehicle):
    pass

##### CHILD #####
class Motorcycle(GroundVehicle):
    pass
