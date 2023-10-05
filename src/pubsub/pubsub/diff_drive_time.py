import matplotlib.pyplot as plt
from math import sin,cos
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3


class diff_drive(Node):
    def __init__(self):
        super().__init__('diff_drive')
        self.sub=self.create_subscription(Vector3, "pos", self.callback, 10)
        self.pub=self.create_publisher(Vector3,"speed",10)
        
        self.model_x=[]
        self.model_y=[]
        self.sim_x=[]
        self.sim_y=[]
        
        self.x=0   #con 
        self.y=0
        self.theta=0

        self.dt=0.05  #con
        self.r=0.05  #con
        self.d=0.15  #con

        self.speed=Vector3()

        self.time=0

    def callback(self, msg):
    
        if self.time<=10:
            self.speed.x=-1.0
            self.speed.y=-1.0
            self.pub.publish(self.speed)

        elif self.time>10 and self.time<=20:
            self.speed.x=-1.5
            self.speed.y=-1.0
            self.pub.publish(self.speed)

        elif self.time>20 and self.time<=30:
            self.speed.x=-1.0
            self.speed.y=-1.5
            self.pub.publish(self.speed)

        elif self.time>30 and self.time<=40:
            self.speed.x=-1.0
            self.speed.y=-1.0
            self.pub.publish(self.speed)

        elif self.time>40:
            self.speed.x=0.0
            self.speed.y=0.0
            self.x=0   #con 
            self.y=0
            self.theta=0
            self.pub.publish(self.speed)

            plt.plot(self.sim_x,self.sim_y,label="sim")
            plt.plot(self.model_x,self.model_y,label="model")
            plt.legend()
            plt.show()
            self.destroy_subscription(self.sub)


        self.v_l=-self.speed.x*self.r  #var
        self.v_r=-self.speed.y*self.r   #var
        self.v_c=(self.v_r+self.v_l)/2   #var

        self.delta_theta=((self.v_r-self.v_l)/self.d)*self.dt
        self.delta_x=self.v_c*cos(self.theta)*self.dt
        self.delta_y=self.v_c*sin(self.theta)*self.dt

        self.theta=self.theta+self.delta_theta
        self.x=self.x+self.delta_x
        self.y=self.y+self.delta_y

        self.sim_x.append(msg.x)
        self.sim_y.append(msg.y)
        self.model_x.append(self.x)
        self.model_y.append(self.y)

        #self.get_logger().info(self.time)
        self.time+=self.dt
        
def main(args=None):
    try:
        rclpy.init(args=args)
        node=diff_drive()
        rclpy.spin(node)
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass