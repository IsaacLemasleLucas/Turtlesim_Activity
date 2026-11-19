#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial
from turtlesim_interfaces.msg import Turtle, TurtleArray
from turtlesim_interfaces.srv import CatchTurtle
from turtlesim.srv import Spawn, Kill
import random


# Node is a client to the service /spawn and /kill
class TurtleSpawnerNode(Node):
    def __init__(self):
        super().__init__("turtle_spawner")
        self.new_turtle = Turtle()
        self.turtles = TurtleArray()
        self.random_position_turtle()
        # Create a timer to call the service spawn every x times
        self.timer_ = self.create_timer(1.0, self.call_turtle_spawner)
        # Publisher of the array of alive turtles
        self.publisher_ = self.create_publisher(TurtleArray, "alive_turtle", 10)
        # Server to call the kill service when a name is received 
        self.server_ = self.create_service(CatchTurtle, "kill_turtle", self.callback_kill_turtle)

    # Function to create the random positions
    def random_position_turtle(self):
        self.new_turtle.x     = random.uniform(0.0,11.0)
        self.new_turtle.y     = random.uniform(0.0,11.0) 
        self.new_turtle.theta = random.uniform(0.0,360.0)

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

        # Publishing the list of alives turtles
        self.turtles.array.append(self.new_turtle)
        self.publisher_.publish(self.turtles)

    def callback_turtle_spawner(self, future, x, y, theta):
        try:
            response = future.result()
            self.get_logger().info("x = " + str(x) + " y = " + str(y) + " theta = " + str(theta))
            self.get_logger().info("Response name = " + str(response.name))
            self.new_turtle.name = response.name
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))

    # Function to call the service kill
    def callback_kill_turtle(self, request, response):
        client = self.create_client(Kill, "kill")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Kill...")
        kill_request = Spawn.Request()
        kill_request.name = request.name
        # future object (Python)
        future = client.call_async(kill_request)
        future.add_done_callback(partial(self.callback_turtle_killer,name=request.name))
        return response

    def callback_turtle_killer(self, future, name):
        try:
            response = future.result()
            self.get_logger().info(f"\nkilled turtle = {name}\n")
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))
   
   
    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawnerNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()