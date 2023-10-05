import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ShapeNode(Node):
    def __init__(self):
        super().__init__("shape_node")
        self.pub=self.create_publisher(String,"shape_topic",10)
        self.get_logger().info("Shape node has been started")
        msg=String()

        while rclpy.ok():
            self.shape=input("Enter the motion: ")
            msg.data=self.shape
            self.pub.publish(msg)


def main (args=None):
    try:
        rclpy.init(args=args)
        node = ShapeNode()
        rclpy.spin(node)
        rclpy.shutdown()

    except KeyboardInterrupt:
        pass