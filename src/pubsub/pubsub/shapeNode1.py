import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from math import *
#import numpy as np

class shapeNode(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(String,'shape_selection',self.listener_callback,10)
        #self.subscription  # prevent unused variable warning
        self.shape=""
        self.publisher= self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.time=0

        #self.theta = np.linspace(0, 2 * np.pi, 1000)  # Adjust the range as needed
        self.create_timer(0.1, self.timer_callback)
    
    def listener_callback(self, msg):
        self.shape = msg.data
        self.get_logger().info('I heard: "%s"' % msg.data)




    def timer_callback(self):
        self.shape_msg =Twist()
        if self.shape=='circle':
            self.shape_msg.linear.x = cos(self.time)
            self.shape_msg.linear.y = sin(self.time)
            self.time+=0.1

        self.publisher.publish(self.shape_msg)
        """"
        if self == 'Rose - Rhodonea':


            

            self.r = cos(4 * self.theta)
            self.shape_msg.linear.x = self.r * cos(self.theta)
            self.shape_msg.linear.y = self.r * sin(self.theta)      

        elif msg =='Spiral Curve':
            self.r = 0.001 * self.theta**2
            self.shape_msg.linear.x = self.r * cos(self.theta)
            self.shape_msg.linear.y = self.r * sin(self.theta)   
            self.time+=0.1

        elif msg =='Flower Shape':

            self.r = sin(5/4 * self.theta)
            self.shape_msg.linear.x = self.r * cos(self.theta)
            self.shape_msg.linear.y = self.r * sin(self.theta)   

        elif msg =='Rounded gear':
        
            self.r = cos(sin(5 * self.theta))
            self.shape_msg.linear.x = self.r * cos(self.theta)
            self.shape_msg.linear.y = self.r * sin(self.theta)
        
        elif msg =='Butterfly':

            self.r = tan(cos(4 * self.theta)) + sin(3 * self.theta)
            self.shape_msg.linear.x = self.r * cos(self.theta)
            self.shape_msg.linear.y = self.r * sin(self.theta)
            
        """

        


        


def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = shapeNode()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


#if __name__ == '__main__':
    #main()
