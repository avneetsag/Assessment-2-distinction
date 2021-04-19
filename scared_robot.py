import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from pynput import keyboard
import getpass

class ScaredRobot(Node):
   
    def listener_callback(self, msg):
        print(msg.data)
        self.get_logger().info('yes')
        front = int(msg.data[:-2]) #remove the 'cm' and convert to int.
        print(front)
        if front > 10:
            msg.data = "CONTF:0010"
            self.publisher.publish(msg)
        
    def listener_callback2(self, msg):
        print(msg.data)
        right = int(msg.data[:-2]) #remove the 'cm' and convert to int.
        print(right)
        if right > 10:
            msg.data = "CONTF:0010"
            self.publisher.publish(msg)    
        if right < 10:
            msg.data = "TURNL:0010"
            self.publisher.publish(msg) 
        
    def listener_callback3(self, msg):
        left = int(msg.data[:-2])
        print(left)
        if left > 10:
            msg.data = "CONTF:0010"
            self.publisher.publish(msg)
        if left < 10:
            msg.data = "TURNR:0010"
            self.publisher.publish(msg)
                   
   
    def __init__(self):
        super().__init__('ScaredRobot')
        self.publisher = self.create_publisher(String, '/robot/control', 10)

        self.subscription = self.create_subscription(
            String,
            '/robot/front',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        self.subscription = self.create_subscription(
            String,
            '/robot/right',
            self.listener_callback2,
            10)
        self.subscription = self.create_subscription(
            String,
            '/robot/left',
            self.listener_callback3,
            10)
        self.subscription  # prevent unused variable warning
               

def main(args=None):
    rclpy.init(args=args)

    scaredrobot = ScaredRobot()
    rclpy.spin(scaredrobot)
    
    scaredrobot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

