import roslib; roslib.load_manifest('ackermann_msgs')
from ackermann.msg import AckermannDrive
from morse.middleware.ros import ROSReader

class AckermannDriveReader(ROSReader):
    """ Subscribe to a motion command and set steer angle and force local data. """
    ros_class = AckermannDrive

    def update(self, message):
        self.data["steer"] = message.steer_angle
        if (abs(message.speed)<0.01):
            self.data["force"] = 0
            self.data["brake"] = 10000
        else
            self.data["force"] = message.speed*10000
            self.data["brake"] = 0  
