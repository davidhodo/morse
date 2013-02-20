import roslib; roslib.load_manifest('ackermann_msgs')
from ackermann_msgs.msg import AckermannDrive
from morse.middleware.ros import ROSReader

class AckermannDriveReader(ROSReader):
    """ Subscribe to a motion command and set steer angle and force local data. """
    ros_class = AckermannDrive

    def update(self, message):
        self.data["steer"] = message.steering_angle
        if (abs(message.speed)<0.01):
            self.data["force"] = 0
            self.data["brake"] = 100
        else:
            self.data["force"] = message.speed*1
            self.data["brake"] = 0  
