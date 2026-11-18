#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial

from turtlesim_interfaces.msg import Turtle
from turtlesim.srv import Spawn
import random


# Node is a client to the service /spawn and /kill
class TurtleSpawnerNode(Node):
    def __init__(self):
        super().__init__("turtle_spawner")
        self.new_turtle = Turtle()
        self.random_position_turtle()
        # Create a timer to call the service spawn every x times
        self.timer_ = self.create_timer(1.0, self.call_turtle_spawner)
        # self.publisher_ = self.create_publisher(Turtle, "alive_turtle", 10)

    # Function to create the random positions
    def random_position_turtle(self):
        self.new_turtle.x     = random.uniform(0.0,11.0)
        self.new_turtle.y     = random.uniform(0.0,11.0) 
        self.new_turtle.theta = random.uniform(0.0,360.0)
        # self.x     = random.uniform(0.0,11.0)
        # self.y     = random.uniform(0.0,11.0)
        # self.theta = random.uniform(0.0,360.0)

    # Function to call the service spawn
    def call_turtle_spawner(self):
        self.random_position_turtle()
        client = self.create_client(Spawn, "spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Spawner...")
    
        request = Spawn.Request()
        request.x = self.new_turtle.x
        request.y = self.new_turtle.y
        request.theta = self.new_turtle.theta

        # future object (Python)
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_turtle_spawner,x=self.new_turtle.x, 
                                         y=self.new_turtle.y, 
                                         theta=self.new_turtle.theta))

        self.get_logger().info(f"New Turtle Data : Name = {self.new_turtle.name} & x,y = {self.new_turtle.x},{self.new_turtle.y}")


    
    def callback_turtle_spawner(self, future, x, y, theta):
        try:
            response = future.result()
            self.get_logger().info("x = " + str(x) + " y = " + str(y) + " theta = " + str(theta))
            self.get_logger().info("Response name = " + str(response.name))
            self.new_turtle.name = response.name
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))
   
    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawnerNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()