#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
    
    
class TurtleControl(Node):
    def __init__(self):
        super().__init__("turtle_control")
        self.get_logger().info("The node turtle_control has been started.")
        self.publisher_ = self.create_publisher(Twist, "Turtle1/cmd_vel", 10)
        timer_period = 0.5
        self.timer_ = self.create_timer(timer_period, self.velocity_callback)
    
    def velocity_callback(self):
        msg = Twist()
        msg.linear.x = 1.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 1.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0
        self.publisher_.publish(msg)
    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControl()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()