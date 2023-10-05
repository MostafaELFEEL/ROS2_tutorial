from setuptools import find_packages, setup

package_name = 'pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='elfeel',
    maintainer_email='elfeel@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub = pubsub.pub:main',
            'sub = pubsub.sub:main',
            'client = pubsub.client:main',
            'server = pubsub.server:main',
            'pub_cmsg = pubsub.pub_cmsg:main',
            'sub_cmsg = pubsub.sub_cmsg:main',
            'shapeNode = pubsub.shapeNode:main',
            'turtleCommander = pubsub.turtleCommander:main',
            'gui = pubsub.GUI:main',
            'shapeNode1 = pubsub.shapeNode1:main',
            'coppelia=pubsub.coppelia:main',
            'diffdrive=pubsub.diff_drive:main',
            'model=pubsub.model:main',
            'diffdrivetime=pubsub.diff_drive_time:main',
        ],
    },
)
