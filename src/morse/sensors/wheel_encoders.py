import GameLogic
import math
import morse.core.sensor

class WheelEncodersClass(morse.core.sensor.MorseSensorClass):
    """ Odometer sensor """

    def __init__(self, obj, parent=None):
        """ Constructor method.

        Receives the reference to the Blender object.
        The second parameter should be the name of the object's parent.
        """
        print ("######## ODOMETER '%s' INITIALIZING ########" % obj.name)
        # Call the constructor of the parent class
        super(self.__class__,self).__init__(obj, parent)

        # Variables to store the accumulated rotation of the 4 wheels
        # if only two wheels are present, only the front right and left 
        # will have values
        self.local_data['rotFR'] = 0.0
        self.local_data['rotFL'] = 0.0
        self.local_data['rotRR'] = 0.0
        self.local_data['rotRL'] = 0.0
        self.local_data['numWheels'] = self.robot_parent.vehicle.getNumWheels()
        print ('######## ODOMETER INITIALIZED ########')


    def default_action(self):
        """ Get the accumulated rotation of each wheel
        """
        # wheel #  -   wheel
        #    0     -    FR
        #    1     -    FL
        #    2     -    RR
        #    3     -    RL
        
        # check to see how many wheels there are:
        
        
        if (self.local_data['numWheels']==2):
            self.local_data['rotFR'] = self.robot_parent.vehicle.getWheelRotation(0)
            self.local_data['rotFL'] = self.robot_parent.vehicle.getWheelRotation(1)
        elif (self.local_data['numWheels']==4):        
            self.local_data['rotFR'] = self.robot_parent.vehicle.getWheelRotation(0)
            self.local_data['rotFL'] = self.robot_parent.vehicle.getWheelRotation(1)
            self.local_data['rotRR'] = self.robot_parent.vehicle.getWheelRotation(2)
            self.local_data['rotRL'] = self.robot_parent.vehicle.getWheelRotation(3)

        
        
