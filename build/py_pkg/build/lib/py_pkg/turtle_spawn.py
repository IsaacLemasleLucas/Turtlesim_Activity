#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial

# from turtlesim_interfaces.srv import CatchTurtle
from turtlesim.srv import Spawn
import random


# Node is a client to the service /spawn and /kill
class TurtleSpawnerClient(Node):
    def __init__(self):
        super().__init__("turtle_spawner")
        self.random_position_turtle()
        # Create a timer to call the service spawn every x times
        self.timer_ = self.create_timer(1.0, self.call_turtle_spawner)

    # Function to create the random positions
    def random_position_turtle(self):
        self.x     = random.uniform(0.0,11.0)
        self.y     = random.uniform(0.0,11.0)
        self.theta = random.uniform(0.0,360.0)
    
    def call_turtle_spawner(self):
        self.random_position_turtle()
        client = self.create_client(Spawn, "spawn")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Spawner...")
    
        request = Spawn.Request()
        request.x = self.x
        request.y = self.y
        request.theta = self.theta

        # future object (Python)
        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_turtle_spawner,x=self.x, y=self.y, theta=self.theta))
    
    def callback_turtle_spawner(self, future, x, y, theta):
        try:
            response = future.result()
            self.get_logger().info("x = " + str(x) + " y = " + str(y) + " theta = " + str(theta))
            self.get_logger().info("Response name = " + str(response.name))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))
            
    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawnerClient()
    rclpy.spin(node)
    rclpy.shutdown()
    
    
if __name__ == "__main__":
    main()