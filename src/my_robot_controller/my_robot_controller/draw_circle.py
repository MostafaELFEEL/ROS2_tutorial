import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MyNode(Node):

    def __init__(self):
        super().__init__("Second_node")
        self.get_logger().info("Draw Circle Node has started")
        self.cmd_vel_pub_ = self.create_publisher(Twist,'/turtle1/cmd_vel', 10)
        self.create_timer(0.5, callback = self.timer_callback)

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)

def main(args = None):
    try:
        rclpy.init(args=args)
        node = MyNode()
        rclpy.spin(node)
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass