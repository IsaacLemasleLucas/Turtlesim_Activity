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

        # --- Declaration of parameters --- #
        self.declare_parameter("linear_x",0.5)
        self.declare_parameter("linear_y",0.0)
        self.declare_parameter("linear_z",0.0)
        self.declare_parameter("angular_x",0.0)
        self.declare_parameter("angular_y",0.0)
        self.declare_parameter("angular_z",0.5)
        self.declare_parameter("timer_period", 0.5)

        # --- Initialisation of current position of the turtle --- #
        self.pos_x     = 0.0
        self.pos_y     = 0.0
        self.pos_theta = 0.0

        # --- Goal to reach --- #
        self.goal_x     = 8.0
        self.goal_y     = 6.0

        # --- Publisher, subscriber & timer --- #
        self.publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(self.get_parameter("timer_period").value, self.velocity_callback)

        self.subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.position_callback, 10)


    def velocity_callback(self):
        msg = Twist()

        # Distance to goal : 
        dist = ((self.goal_x - self.pos_x)**2 + (self.goal_y - self.pos_y)**2)**(0.5)
        # Angle to goal :
        goal_theta = math.atan2((self.goal_y - self.pos_y),(self.goal_x - self.pos_y))
        # Difference between angles :
        diff_theta = goal_theta - self.pos_theta 
        # normalisation of diff theta :
        diff_theta = math.atan2(math.sin(diff_theta),math.cos(diff_theta))
        # Direction for the goal :
        if  diff_theta > 0.05 :
            msg.angular.z = 0.1
            msg.linear .x = 0.0
            self.get_logger().info(f"PLUS")
        elif diff_theta < -0.05:    
            msg.angular.z = -0.1
            msg.linear .x = 0.0

            self.get_logger().info(f"MOINS")
        else:
            msg.angular.z = 0.0
            # Go to the goal :
            if dist > 0.1 :
                msg.linear.x = 0.5
            else:
                msg.linear.x = 0.0
        self.get_logger().info(f"Distance = {dist}, Diff Theta = {diff_theta}")
        # --- Publish the message --- #
        self.publisher_.publish(msg)

    def position_callback(self, msg):
        self.pos_x = msg.x 
        self.pos_y = msg.y 
        self.pos_theta = msg.theta 
        # l_velocity = msg.linear_velocity  
        # a_velocity = msg.angular_velocity 
        # self.get_logger().info(f"Positions of turtle : x = {self.pos_x}, y = {self.pos_y}, theta = {self.pos_theta} ")
        # self.get_logger().info(f"Velocity of turtle : Linear = {l_velocity}, Angular = {a_velocity}")
    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControlNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()