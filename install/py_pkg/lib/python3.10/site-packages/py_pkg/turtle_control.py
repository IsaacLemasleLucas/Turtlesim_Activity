#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
    
    
class TurtleControl(Node):
    def __init__(self):
        super().__init__("turtle_control")
        self.get_logger().info("The node turtle_control has been started.")

        # Declaration of parameters
        self.declare_parameter("linear_x",1.0)
        self.declare_parameter("linear_y",0.0)
        self.declare_parameter("linear_z",0.0)
        self.declare_parameter("angular_x",0.0)
        self.declare_parameter("angular_y",0.0)
        self.declare_parameter("angular_z",0.5)
        self.declare_parameter("timer_period", 0.5)

        self.publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(self.get_parameter("timer_period").value, self.velocity_callback)
    
    def velocity_callback(self):
        msg = Twist()
        msg.linear.x = self.get_parameter("linear_x").value
        msg.linear.y = self.get_parameter("linear_y").value
        msg.linear.z = self.get_parameter("linear_z").value
        msg.angular.x = self.get_parameter("angular_x").value
        msg.angular.y = self.get_parameter("angular_y").value
        msg.angular.z = self.get_parameter("angular_z").value
        self.publisher_.publish(msg)
    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControl()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()