import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from std_msgs.msg import String
from math import sin,cos


class TurtleCommander(Node):
    def __init__(self):
        super().__init__('turtle_commander')
        self.create_subscription(String,"shape_topic",self.listener_callback,10)
        self.pub=self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.get_logger().info("Turtle Commander has been started")
        self.i=0
        self.shape=""
        self.delta_t=0.1
        self.msg=Twist()
        self.create_timer(self.delta_t,self.callback_timer)
        
    def listener_callback(self,msg):
        self.get_logger().info(str(msg.data))
        self.shape=msg.data
    

    def callback_timer(self):


        if self.shape=="heart":
            self.msg.linear.x= 0.1*(48*pow(sin(self.i),2)*cos(self.i))
            self.msg.linear.y= 0.1*(-13*sin(self.i)+10*sin(2*self.i)+6*sin(3*self.i)+4*sin(4*self.i))
            self.pub.publish(self.msg)
            self.i+=self.delta_t

        elif self.shape=="star":
            self.msg.linear.x = 0.3*((-2*sin(self.i)) - ((5*(2/3))*sin((2/3)*self.i)))
            self.msg.linear.y = 0.3*((2*cos(self.i)) - ((5*(2/3))*cos((2/3)*self.i)))
            self.pub.publish(self.msg)
            self.i+=self.delta_t


        
        elif self.shape=="stop":
            self.msg.linear.x=0.0
            self.msg.linear.y=0.0
            self.msg.linear.z=0.0
            self.msg.angular.x=0.0
            self.msg.angular.y=0.0
            self.msg.angular.z=0.0
            self.pub.publish(self.msg)
            self.i+=self.delta_t

        elif self.shape=="epicycloid":
            self.msg.linear.x=0.5*(-4*sin(self.i)+4*sin(4*self.i))
            self.msg.linear.y=0.5*(4*cos(self.i)-4*cos(4*self.i))
            self.pub.publish(self.msg)
            self.i+=self.delta_t

        
            


def main(args=None):
    rclpy.init(args=args)
    node=TurtleCommander()
    rclpy.spin(node)
    rclpy.shutdown()




"""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from math import sin,cos



class Mynode(Node):
    def __init__(self):
        super().__init__("DrawCircle")
        self.cmv_vel_pub_= self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_subscription(String,"/draw/input",self.sub_Callback,10)
        self.get_logger().info("Drawing Started")
        self.shapes=["circle","astroid","end", "flower"]
        self.drawing="" 
        self.t=0
        self.msg = Twist()
        self.create_timer(0.1,self.Draw)

    
    def sub_Callback(self,msg):
        for s in self.shapes:
            if s == msg.data:
                self.drawing=msg.data
                break

    def Draw(self):

        if(self.drawing =="circle"):
            pass


        elif(self.drawing == "astroid"):
            pass


        elif(self.drawing == "end"):
            pass

        elif(self.drawing == "flower"):
            self.msg.linear.x=4*cos(self.t)*cos(4*self.t)-sin(self.t)*sin(4*self.t)
            self.msg.linear.y=4*cos(4*self.t)*sin(self.t)+sin(4*self.t)*cos(self.t)
            self.cmv_vel_pub_.publish(self.msg)
            self.t+=0.1

def main(args=None):
    rclpy.init(args=args)
    node=Mynode()
    rclpy.spin(node)
    rclpy.shutdown()

    """
"""
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import String
from math import sin,cos

def main(args=None):
    global draw,t,node,msg
    rclpy.init(args=args)
    node=Node()
    node.__init__("DrawCircle")
    super(node).__init__("DrawCircle")
    
    node.pub=node.create_publisher(Twist,"/turtle1/cmd_vel",10)
    node.create_subscription(String,"/draw/input",node.sub_Callback,10)
    node.get_logger().info("Drawing Started")
    draw=""
    t=0
    msg=Twist()
    node.create_timer(0.1,node.Draw)
    

    rclpy.spin(node)
    rclpy.shutdown()

def sub_Callback(msg):
    global draw
    draw=msg.data

def Draw(self):
    if(draw=="flower"):
        msg.linear.x=4*cos(t)*cos(4*t)-sin(t)*sin(4*t)
        msg.linear.y=4*cos(4*t)*sin(t)+sin(4*t)*cos(t)
        node.pub.publish(msg)
        self.t+=0.1

"""