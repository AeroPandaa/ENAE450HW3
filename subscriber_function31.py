import rclpy
from rclpy.node import Node
from std_msgs.msg import UInt32MultiArray




class SubSort(Node):

    def __init__(self):
        super().__init__('subsort')
        #create subscriptions
        self.sub1 = self.create_subscription(UInt32MultiArray, 'topic_1', self.sub1_callback, 10)
        self.sub2 = self.create_subscription(UInt32MultiArray, 'topic_2', self.sub2_callback,  10)
        # does not like this line self.subscription  # prevent unused variable warning



        ######### BONUS ( __init__) #########
                    #not working
        #create publisher
        #self.pub3 = self.create_publisher(UInt32MultiArray, 'topic_3', 10)
         # repeat at 0.5 Hz 
        #timer_period = 2  # seconds
        #create timers
        #self.timer1 = self.create_timer(timer_period, self.sub2_callback)
        #create counter
        #self.i = 1
        ######### BONUS #########
    

    def sub1_callback(self, msg):
        self.list1 = msg.data.tolist()
        #self.get_logger().info('I heard something %s' % self.list1)

    
    def sub2_callback(self, msg):
        self.list2 = msg.data.tolist()
        #self.get_logger().info('I heard something %s' % self.list2)
        
        if self.list1[0]==self.list2[0]:
            #get the serial number and remove the other
            ser = self.list1.pop(0)
            rmser = self.list2.pop(0)
            #merge and then merge sort list
            list3 = []
            #idk why i can just add these in one line?
            list3.extend(self.list1)
            list3.extend(self.list2)
            #merge sort them
            self.list4 = self.mergeSort(list3)
            #print to console
            self.get_logger().info('Serial list sorted: ' + str(ser) + '\n%s\n\n' % self.list4)
           # self.get_logger().info('The merged and sorted list is: %s' % list4)
            self.list1 = []
            self.list2 = []

            ##### BONUS (callback/publish) #####
            
        
            #msgout = UInt32MultiArray()
            #fill message
            #bonusList = self.list4
            #msgout.data = bonusList
            #publish
            #self.pub3.publish(msgout)
            #print to check
            #self.get_logger().info('\n\nPublishing topic_3: %s' % msgout.data)
            #self.i += 1
            ##### BONUS #####
      


        

            

    def mergeSort(self,list):
        if len(list)>1:

            #finding the middle of the list, and setting into two halves
            mid = len(list)//2
            lefthalf = list[:mid]
            righthalf = list[mid:]

            #sort both halves, how do we call the function we are creating?
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)

            #keep track of iterations
            i=0
            j=0
            k=0
            
            #put data in temporary list
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] <= righthalf[j]:
                    list[k]=lefthalf[i]
                    i=i+1
                else:
                    list[k]=righthalf[j]
                    j=j+1
                k=k+1
                #last check
            while i < len(lefthalf):
                list[k]=lefthalf[i]
                i=i+1
                k=k+1
            while j < len(righthalf):
                list[k]=righthalf[j]
                j=j+1
                k=k+1
            
        return(list)

def main(args=None):
    rclpy.init(args=args)
    subsort = SubSort()
    rclpy.spin(subsort)
    subsort.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
