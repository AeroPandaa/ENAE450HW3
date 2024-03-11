import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt32MultiArray



class PubSort(Node):

    def __init__(self):
        super().__init__('PubSort')
        #create publishers
        self.pub1 = self.create_publisher(UInt32MultiArray, 'topic_1', 10)
        self.pub2 = self.create_publisher(UInt32MultiArray, 'topic_2', 10)
        # repeat at 0.5 Hz 
        timer_period = 2  # seconds
        #create timers
        self.timer1 = self.create_timer(timer_period, self.list1_callback)
        self.timer2 = self.create_timer(timer_period, self.list2_callback)
        #create counters
        self.i = 1
        self.k = 1

    def list1_callback(self):
        #give message a type
        msg = UInt32MultiArray()
        #fill message
        list1 = self.randomGen()
        list1.insert(0,self.i)
        msg.data = list1
        list1b = msg.data.tolist()
        #publish
        self.pub1.publish(msg)
        #print to check
        self.get_logger().info('Publishing topic_1: %s' % list1b)
        #increase the counter
        self.i += 1

    def list2_callback(self):
        #give message a type
        msg = UInt32MultiArray()
        #fill message
        list2 = self.randomGen()
        list2.insert(0,self.k)
        msg.data = list2
        list2b = msg.data.tolist()
        #publish
        self.pub2.publish(msg)
        #print to check
        self.get_logger().info('Publishing topic_2: %s' % list2b)
        #increase the counter
        self.k += 1       

    def randomGen(self):
        return [random.randint(1,100) for _ in range(10)]

def main(args=None):
    rclpy.init(args=args)
    pubsort = PubSort()
    rclpy.spin(pubsort)
    pubsort.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
