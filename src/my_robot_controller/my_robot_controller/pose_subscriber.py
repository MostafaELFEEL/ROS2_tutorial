import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class Subscriber_Node(Node):
    
    def __init__(self):
        super().__init__("Subscriber_Node")
        self.pose_sub_ = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)

    def pose_callback(self, msg: Pose):
        print(msg)
    

def main(args=None):
    try:
        rclpy.init(args=args)
        node = Subscriber_Node()
        rclpy.spin(node)
        rclpy.shutdown()

    except KeyboardInterrupt:
        pass