from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='pubsub',
            namespace='',
            executable='turtleCommander',
            name='turtleCommander'
        ),
        
        Node(
            package='turtlesim', 
            namespace='', 
            executable='turtlesim_node',
            name='turtlesim_node' 
        )
    ])