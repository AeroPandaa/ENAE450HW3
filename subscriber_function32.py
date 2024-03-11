import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt32MultiArray




class SubSort(Node):

    def __init__(self):
        super().__init__('subsort')
        #create subscriptions
        self.sub1 = self.create_subscription(UInt32MultiArray, 'topic_1', self.list_callback, 10)
        self.sub2 = self.create_subscription(UInt32MultiArray, 'topic_2', self.int_callback,  10)
        # does not like this line self.subscription  # prevent unused variable warning
    

    def list_callback(self, msg):
        self.list1 = msg.data.tolist()
        #self.get_logger().info('I heard something %s' % self.list1)

    
    def int_callback(self, msg):
        self.list2 = msg.data.tolist()
        #self.get_logger().info('I heard something %s' % self.list2)
        
        if self.list1[0]==self.list2[0]:
            ser = self.list1.pop(0)
            rmser = self.list2.pop(0)

            t = self.search(self.list1,self.list2)
            self.get_logger().info('Serial number: %s' % ser)
            self.get_logger().info('The integer is: %s' % self.list2) # assuming it has been popped
            if t == 0:
                self.get_logger().info('False! Number not found.\n')
            else:
                self.get_logger().info('True! The number was found.\n')
            self.list1 = []
            self.list2 = []



    def search(self,list1,intlist):
        t = 0
        k = 0
        for x in list1:
            if list1[k]==intlist[0]: # assumes serial has been popped
                t = 1
            k += 1
        return t

def main(args=None):
    rclpy.init(args=args)
    subsort = SubSort()
    rclpy.spin(subsort)
    subsort.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
