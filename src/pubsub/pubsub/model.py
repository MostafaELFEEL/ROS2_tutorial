import matplotlib.pyplot as plt
from math import sin,cos
import rclpy
from rclpy.node import Node

class model(Node):
    def __init__(self):
        super().__init__('diff_drive')
        
        self.model_x=[]
        self.model_y=[]
        self.w_l=3
        self.w_r=3
        self.r=0.05
        self.v_l=self.w_l*self.r
        self.v_r=self.w_r*self.r
        self.v_c=(self.v_r+self.v_l)/2
        self.l=0.15
        self.dt=0.1
        self.x=0
        self.y=0
        self.theta=0
        self.delta_x=0
        self.delta_y=0
        self.delta_theta=0
        self.timer=self.create_timer(self.dt,self.callback)
        self.i=0

        

    def callback(self):

        self.delta_theta=((self.v_r-self.v_l)/self.l)*self.dt
        
        self.delta_x=self.v_c*cos(self.theta)*self.dt
        self.delta_y=self.v_c*sin(self.theta)*self.dt

        self.theta=self.theta+self.delta_theta
        self.x=self.x+self.delta_x
        self.y=self.y+self.delta_y

        self.model_x.append(self.x)
        self.model_y.append(self.y)
        self.i+=self.dt
        if self.i >= 10:
            plt.plot(self.model_x,self.model_y,label="model")
            plt.legend()
            plt.show()
            self.destroy_timer(self.timer)


        
def main(args=None):
    rclpy.init(args=args)
    node=model()
    rclpy.spin(node)
    rclpy.shutdown()
