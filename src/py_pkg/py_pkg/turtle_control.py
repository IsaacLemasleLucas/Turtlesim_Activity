#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
    
    
class TurtleControlNode(Node):
    def __init__(self):
        super().__init__("turtle_control")
        self.get_logger().info("The node turtle_control has been started.")

        # Declaration of parameters
        self.declare_parameter("linear_x",0.5)
        self.declare_parameter("linear_y",0.0)
        self.declare_parameter("linear_z",0.0)
        self.declare_parameter("angular_x",0.0)
        self.declare_parameter("angular_y",0.0)
        self.declare_parameter("angular_z",0.5)
        self.declare_parameter("timer_period", 0.5)

        # Current position of the turtle
        self.pos_x = 0.0
        self.pos_y = 0.0
        self.pos_theta = 0.0

        # goal to reach
        self.goal_x = -8.0
        self.goal_y = 6.0
        self.goal_theta = 0.0
        self.correction = 0.2
        self.goal_reached = False

        self.publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(self.get_parameter("timer_period").value, self.velocity_callback)

        self.subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.position_callback, 10)

    def goal_direction_compute(self):
        self.goal_theta = math.atan((self.goal_y - self.pos_y)/(self.goal_x - self.pos_y))
    
    def velocity_callback(self):
        msg = Twist()
        self.goal_direction_compute()
        # msg.linear.x = self.get_parameter("linear_x").value
        # msg.linear.y = self.get_parameter("linear_y").value
        # msg.linear.z = self.get_parameter("linear_z").value
        # msg.angular.x = self.get_parameter("angular_x").value
        # msg.angular.y = self.get_parameter("angular_y").value
        # msg.angular.z = self.get_parameter("angular_z").value

        # Going for the goal 
        x_condition = self.pos_x > (self.goal_x + 1) or self.pos_x < (self.goal_x - 1)
        y_condition = self.pos_y > (self.goal_y + 1) or self.pos_y < (self.goal_y - 1)
        if x_condition or y_condition:
            msg.linear.x += 0.5
        else:
            msg.linear.x = 0

        # Direction for the goal
        if self.pos_theta > (self.goal_theta + 0.1):
            msg.angular.z -= self.correction
        elif self.pos_theta < (self.goal_theta - 0.1):
            msg.angular.z += self.correction
        self.publisher_.publish(msg)

    def position_callback(self, msg):
        self.pos_x = msg.x 
        self.pos_y = msg.y 
        self.pos_theta = msg.theta 
        l_velocity = msg.linear_velocity  
        a_velocity = msg.angular_velocity 
        self.get_logger().info(f"Positions of turtle : x = {self.pos_x}, y = {self.pos_y}, theta = {self.pos_theta}")
        self.get_logger().info(f"Velocity of turtle : Linear = {l_velocity}, Angular = {a_velocity}")
    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControlNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()