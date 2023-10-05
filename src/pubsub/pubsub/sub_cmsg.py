import rclpy
from rclpy.node import Node
from custom_message.msg import Test


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(Test,'topic',self.listener_callback,10)
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%d"' % msg.message)


def main():
    rclpy.init()
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    rclpy.shutdown()
