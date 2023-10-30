#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import SetPen
from functools import partial

class MyNode(Node):
    def __init__(self) -> None:
        super().__init__("my_node")
        self.previous_x_ = 0
        self.my_publisher_ = self.create_publisher( Twist, '/turtle1/cmd_vel' , 10 )
        self.my_subcriber_ = self.create_subscription( Pose , '/turtle1/pose' , self.callback , 10)
    
    def callback(self, msg: Pose):

        speed = Twist()
        speed.linear.x = 2.0

        if msg.x > 9 or msg.x < 1 or msg.y > 9 or msg.y < 1:
            speed.angular.z = 5.0
        else:
            speed.angular.z = 0.0
        
        self.my_publisher_.publish(speed)

        if msg.x > 5.5 and self.previous_x_ <= 5.5:
            self.previous_x_ = msg.x
            self.call_set_pen_service(255,0,0,3,0)
        elif msg.x <= 5.5 and self.previous_x_ > 5.5:
            self.previous_x_ = msg.x
            self.call_set_pen_service(50,100,100,3,0)

    def call_set_pen_service( self, r , g , b , width , off ):
        client = self.create_client( SetPen , "/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger.warn("waiting for service")

        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_setpen))

    def callback_setpen(self,future):
        response = future.result()
        

def main(args = None):
    try:
        rclpy.init(args=args)
        node = MyNode()
        rclpy.spin(node)
        rclpy.shutdown()

    except KeyboardInterrupt:
        pass
