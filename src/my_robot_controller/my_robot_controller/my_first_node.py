#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("first_node")
        self.counter_ = 0

        # Create a timer that calls the call back function every second
        self.create_timer(1.0,callback = self.timer_callback)
        
    # call back function to be excuted every one sec
    def timer_callback(self):
        
        self.get_logger().info("the time in seconds is: " + str(self.counter_))
        self.counter_ += 1

def main(args = None):
    rclpy.init(args=args)

    # Write the code here
    # Creating the node of class MyNode
    node = MyNode()

    # keep the Node running until interruption
    rclpy.spin(node)

    # kill the Node 
    rclpy.shutdown()
    

if __name__ == "__main__":
    main()