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
        self.timer1 = self.create_timer(timer_period, self.list_callback)
        self.timer2 = self.create_timer(timer_period, self.int_callback)
        #create counters
        self.i = 1
        self.k = 1

    def list_callback(self):
        #give message a type
        msg = UInt32MultiArray()
        #fill message
        list1 = self.randomGenList()
        #inserting serial number
        list1.insert(0,self.i)
        msg.data = list1
        list1b = msg.data.tolist()
        #publish
        self.pub1.publish(msg)
        #print to check
        self.get_logger().info('Publishing topic_1(list): %s' % list1b)
        #increase the counter
        self.i += 1

    def int_callback(self):
        #give message a type
        msg = UInt32MultiArray()
        #fill message
        list2 = self.randomGenInt()
        #inserting serial
        list2.insert(0,self.k)
        msg.data = list2
        integ = msg.data.tolist()
        #publish
        self.pub2.publish(msg)
        #print to check
        self.get_logger().info('Publishing topic_2(int): %s\n' % integ)
        #increase the counter
        self.k += 1       

    def randomGenList(self):
        return [random.randint(1,100) for _ in range(21)]
    
    def randomGenInt(self):
        return [random.randint(1,100) for _ in range(1)]

def main(args=None):
    rclpy.init(args=args)
    pubsort = PubSort()
    rclpy.spin(pubsort)
    pubsort.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
