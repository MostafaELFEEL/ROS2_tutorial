import matplotlib.pyplot as plt
from math import sin,cos
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from std_msgs.msg import String



class diff_drive(Node):
    def __init__(self):
        super().__init__('diff_drive')

        self.sub=self.create_subscription(Vector3, 'pos', self.callback, 10)
        self.sub1=self.create_subscription(String,'shape_topic',self.callback1,10)
        self.pub=self.create_publisher(Vector3,"speed",10)
        
        self.model_x=[]
        self.model_y=[]
        self.sim_x=[]
        self.sim_y=[]

                
        self.x=0   #con 
        self.y=0
        self.theta=0

        #self.delta_x=0
        #self.delta_y=0
        #self.delta_theta=0

        self.dt=0.05  #con
        self.r=0.05  #con
        self.d=0.15  #con

        self.shape=""

        self.speed=Vector3()

        self.speed.x=0.0
        self.speed.y=0.0

        self.fig, self.ax = plt.subplots()
        
    def callback1(self,msg):
        self.shape=msg.data

        '''
        if msg.data=="start":
            self.sub=self.create_subscription(Vector3, 'pos', self.callback, 10)
            self.x=0   #con 
            self.y=0
            self.theta=0
            self.sim_x=[]
            self.sim_y=[]
            self.model_x=[]
            self.model_y=[]
            '''


    def callback(self, msg):
        #self.get_logger().info(self.shape)
        
        if self.shape=="for":
            self.speed.x=-1.0
            self.speed.y=-1.0
            self.pub.publish(self.speed)

        elif self.shape=="back":
            self.speed.x=1.0
            self.speed.y=1.0
            self.pub.publish(self.speed)
            

        elif self.shape=="left":
            self.speed.x=-1.0
            self.speed.y=-1.5
            self.pub.publish(self.speed)
              #var

        elif self.shape=="right":
            self.speed.x=-1.5
            self.speed.y=-1.0
            self.pub.publish(self.speed)

        elif self.shape=="stop":
            self.speed.x=0.0
            self.speed.y=0.0
            self.x=0
            self.y=0
            self.model_x=[]
            self.model_y=[]
            self.sim_x=[]
            self.sim_y=[]
            self.pub.publish(self.speed)
            self.destroy_subscription(self.sub)

            
            #self.ax.clear()
            


        self.v_l=-self.speed.x*self.r  #var
        self.v_r=-self.speed.y*self.r   #var
        self.v_c=(self.v_r+self.v_l)/2   #var

        self.delta_theta=((self.v_r-self.v_l)/self.d)*self.dt
        self.delta_x=self.v_c*cos(self.theta)*self.dt
        self.delta_y=self.v_c*sin(self.theta)*self.dt

        self.theta=self.theta+self.delta_theta
        self.x=self.x+self.delta_x
        self.y=self.y+self.delta_y

        self.model_x.append(self.x)
        self.model_y.append(self.y)
        self.sim_x.append(msg.x)
        self.sim_y.append(msg.y)


        self.ax.clear()
        self.ax.plot(self.sim_x, self.sim_y, label='Simulation')
        self.ax.plot(self.model_x, self.model_y, label='Model')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.legend()
        #self.update_plot()
        plt.pause(0.00001)  # Add a slight pause to update the plot

        
        
def main(args=None):
    try:
        rclpy.init(args=args)
        node=diff_drive()
        rclpy.spin(node)
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass