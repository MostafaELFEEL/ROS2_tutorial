#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

# message type was obtained using ros2 interface show command
from geometry_msgs.msg import Twist

class MyNode(Node):

    def __init__(self):
        super().__init__("Second_node")

        # Create a timer that calls the call back function every second
        self.get_logger().info("Draw Circle Node has started")
        self.cmd_vel_pub_ = self.create_publisher(Twist,'/turtle1/cmd_vel', 10)
        self.create_timer(0.5, callback = self.timer_callback)



    # call back function to be excuted every one sec
    def timer_callback(self):
        
        #self.get_logger().info("the time in seconds is: " + str(self.counter_))
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)

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