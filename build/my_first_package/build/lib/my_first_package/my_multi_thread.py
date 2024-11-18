import rclpy as rp
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from my_first_package_msgs.action import DistTurtle
from my_first_package.my_subscriber import TurtlesimSubscriber

import math
import time


def main(args=None):
    rp.init(args=args)

    executor = MultiThreadedExecutor()

    ac = DistTurtleServer()
    sub = TurtleSub_Action(ac_server=ac)

    executor.add_node(sub)
    executor.add_node(ac)

    try:
        executor.spin()
    finally:
        executor.shutdown()
        sub.destroy_node()
        ac.destroy_node()
        rp.shutdown()


if __name__ == '__main__':
    main()
