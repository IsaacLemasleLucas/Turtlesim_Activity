#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
from functools import partial
from turtlesim_interfaces.msg import Turtle, TurtleArray
from turtlesim_interfaces.srv import CatchTurtle
    
class TurtleControlNode(Node):
    def __init__(self):
        super().__init__("turtle_control")
        self.get_logger().info("The node turtle_control has been started.")

        # --- Declaration of parameters --- #
        self.declare_parameter("linear_x",0.0)
        self.declare_parameter("linear_y",0.0)
        self.declare_parameter("linear_z",0.0)
        self.declare_parameter("angular_x",0.0)
        self.declare_parameter("angular_y",0.0)
        self.declare_parameter("angular_z",0.0)
        self.declare_parameter("timer_period", 0.01)

        # --- Initialisation of current position of the turtle --- #
        self.pose_ = None

        # --- Goal to reach --- #
        self.goal_x     = 10.0
        self.goal_y     = 2.0
        self.goal_name  = ""

        # --- Publisher, subscriber & timer --- #
        self.publisher_  = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.position_callback, 10)
        self.timer_      = self.create_timer(self.get_parameter("timer_period").value, self.velocity_callback)
        self.subscriber_alive = self.create_subscription(TurtleArray, "alive_turtle", self.alive_turtle_callback, 10)


    def position_callback(self, msg):
        self.pose_ = msg

    def velocity_callback(self):
        if self.pose_ == None:
            return
        
        msg = Twist()

        dist_x   = self.goal_x - self.pose_.x
        dist_y   = self.goal_y - self.pose_.y
        distance = math.sqrt(dist_x*dist_x + dist_y*dist_y)

        if distance > 0.5:
            # Position
            msg.linear.x  = 2* distance

            # Orientation
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose_.theta
            # Normalise the angle 
            if diff > math.pi :
                diff -= 2*math.pi
            elif diff < -math.pi :
                diff += 2*math.pi
            
            msg.angular.z = 6* diff
        else:
            msg.linear.x  = 0.0
            msg.angular.z = 0.0
            self.call_kill_the_turtle(self.goal_name)
            
        # --- Publish the message --- #
        self.publisher_.publish(msg)

    def alive_turtle_callback(self, msg):
        self.get_logger().info(f"\n\nLast turtle = {msg.array[-1].name}\n")
        self.goal_x    = msg.array[-1].x
        self.goal_y    = msg.array[-1].y
        self.goal_name = msg.array[-1].name

    def call_kill_the_turtle(self, name_to_kill):
        client = self.create_client(CatchTurtle, "kill_turtle")
        while not client.wait_for_service(1.0):
            self.get_logger().info(f"Waiting for service Turtle Killer...")
        request = CatchTurtle.Request()
        request.name = name_to_kill
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_kill_that_name, name=name_to_kill))

    def callback_kill_that_name(self, future, name):
        try:
            response = future.result()
            self.get_logger().info(f"The turtle to kill is {response.name}")
        except Exception as e :
            self.get_logger().info(f"Service call failed %r" % (e,))
    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControlNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
if __name__ == "__main__":
    main()