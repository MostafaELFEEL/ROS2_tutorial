import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32,Float64MultiArray
from nav_msgs.msg import Odometry, Path
import math
import tf_transformations
from numpy import pi

#####################################################################
####          Skeleton code for controller node                  ####
####    Feel free to change/ add functions as you wish           ####
####    You can also change the arguments of the functions       ####
####    Note: Don't alter the node name                          ####
#####################################################################

class Controller(Node):
    def __init__(self):
        super().__init__('controller')
        self.sub1=self.create_subscription(Path, '/path', self.pathCallback, 10)
        self.create_subscription(Odometry, '/state', self.stateCallback, 10)
        self.steering_pub = self.create_publisher(Float32, '/steer', 10)
        self.throttle_pub = self.create_publisher(Float32, '/throttle', 10)
        self.create_subscription(Float64MultiArray,"/pid",self.pid_callback,10)



        self.t=0.1
        self.create_timer(self.t, self.timer_callback)

        self.l=2.5
        self.lookahead=5

        self.targetvel=0

        self.path=None
        self.targetIndex=0
        self.pose=None
        self.quaternion=0
        self.theta=0
        self.targetpose=0
        self.vel=0
        self.acc=0
        self.targetangle=0
        self.steeringangle=0

        self.kp=0.1  #0.1
        self.ki=0.0001  #0.0001
        self.kd=0.00001  #0.00001

        self.throttle=0
        
        ### Initialize publishers and subscribers here ###

    def pid_callback(self,msg):

        self.kp=msg.data[0]
        self.ki=msg.data[1]
        self.kd=msg.data[2]



    def timer_callback(self):

        if self.pose!=None and self.path!=None:
                
                self.vel_function()
                self.searchTargetPoint()
                self.purePursuit()
                self.pidController()

                #self.get_logger().info('Target Index: %d' % self.targetIndex)
                ### Timer callback function ###
                ###done###

    def vel_function(self):
            if math.dist(self.pose,self.path[-1])<14:
                self.targetvel=0
            else:
                self.targetvel=8

            

    def stateCallback(self, state:Odometry):

        self.pose=[state.pose.pose.position.x,state.pose.pose.position.y]
        self.vel=state.twist.twist.linear.x
        self.quaternion=[state.pose.pose.orientation.x,state.pose.pose.orientation.y,state.pose.pose.orientation.z,state.pose.pose.orientation.w]

        self.get_logger().info('speed: %f' % self.vel)
        self.get_logger().info('Target Velocity: %f' % self.targetvel)

        self.theta=tf_transformations.euler_from_quaternion(self.quaternion)[2]

        #self.get_logger().info('State')
        ### Call back function for state message ###
        ###done###

    def pathCallback(self, path:Path):
        self.path=[]
        for i in range(len(path.poses)):
            self.path.append([path.poses[i].pose.position.x,path.poses[i].pose.position.y])

        if self.pose!=None and self.path!=None:


            smallestdistance=math.dist(self.pose,self.path[0])

            for i in range(len(self.path)):

                if math.dist(self.pose,self.path[i])<=smallestdistance:
                    smallestdistance=math.dist(self.pose,self.path[i])
                    self.targetIndex=i

            self.targetpose=self.path[self.targetIndex]

            #self.get_logger().info('Path')
            self.destroy_subscription(self.sub1)
            ### Call back function for path message ###
            ###done###

    def pidController(self):

        
        self.acc=(self.targetvel-self.vel)/self.t

        self.throttle=self.kp*(self.acc)+self.ki*(self.acc*self.t)+self.kd*((self.acc)/self.t)

        #self.get_logger().info('Throttle: %f' % self.throttle)

        if self.throttle>1:
            self.throttle=1

        if self.throttle<-1:
            self.throttle=-1

        msg1=Float32()
        msg1.data=float(self.throttle)

        self.throttle_pub.publish(msg1)

        ###            Implement PID controller here                   ###
        #          Take as an input the current state of the car         #
        #                   Return acceleration                          #
    
    def searchTargetPoint(self):
                
        while math.dist(self.pose,self.path[self.targetIndex])<self.lookahead:
            if self.targetIndex==len(self.path)-1:
                break
            self.targetIndex+=1

        self.targetpose=self.path[self.targetIndex]

        ###           Search for target point in the given path               ###
        #       Take as an input the current state of the car & waypoints       #
        #                   Return index of target point                        #
        #done#

    def purePursuit(self):

        self.targetangle=math.atan2(self.targetpose[1]-self.pose[1],self.targetpose[0]-self.pose[0])-self.theta

        self.steeringangle=math.atan2(2*self.l*math.sin(self.targetangle),self.lookahead)

        self.steeringangle=self.steeringangle*180/pi

        #self.get_logger().info('Steering Angle: %f' % self.steeringangle)


        if self.steeringangle>35:
            self.steeringangle=35

        if self.steeringangle<-35:
            self.steeringangle=-35

        if self.targetIndex!=len(self.path)-1:
            msg2=Float32()
            msg2.data=float(self.steeringangle)
            self.steering_pub.publish(msg2)

        
        
        ###              Implement pure pursuit controller here               ###
        #            Take as an input the current state of the car,             #
        #                     waypoints & targetIndex                           #
        #                      Return steering angle                            #
        ###done###

def main(args=None):

    try:
        rclpy.init(args=args)
        controller = Controller()
        rclpy.spin(controller)
        controller.destroy_node()
        rclpy.shutdown()  
    except KeyboardInterrupt:
        pass     
