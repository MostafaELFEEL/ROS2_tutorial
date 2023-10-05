from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pubsub',
            namespace='pubsub',
            executable='sub',
            name='sub'
        ),
        Node(
            package='pubsub', 
            namespace='pubsub', 
            executable='pub',
            name='pub' 
        )
    ])