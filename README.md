# Stephen McGowan HW3 ENAE450

1. Choose your src folder within your workspace and source ros2
```bash
clear
cd ~/home/ENAE450_hw_ws/hw3/src
source /opt/ros/humble/setup.bash
```
2. Clone my repository to get the publisher and subscriber functions
```bash
cd ..
git clone https://github.com/AeroPandaa/ENAE450HW3.git
```
3. Create packages
```bash
cd src
#ros2 pkg create --build-type ament_python <package_name>
ros2 pkg create --build-type ament_python hw3_1
ros2 pkg create --build-type ament_python hw3_2
```
4. Copy files from cloned repository to second layer of package 
```bash
# i.e copy the publisher_function31.py and subscriber_function31.py to something like /home/stephenlinux/home/ENAE450_hw_ws/hw3/src/hw3_1/hw3_1
```
5. Delete package.xml and setup.py files that were automatically generated in the first layer of the package and replace with the ones from the cloned repository
```bash
# i.e copy the package.xml and setup.py to something like /home/stephenlinux/home/ENAE450_hw_ws/hw3/src/hw3_1
```
6. Return to workspace and build the packages
```bash
cd ..
colcon build --packages-select hw3_1
colcon build --packages-select hw3_2
```
7. Split your terminal window however you shoose
```bash
# i.e 2 or 3 windows
```
8. In window 1 run 
```bash
source install/setup.bash
ros2 run hw3_1 pub
```
9. In the other window run 
```bash
source install/setup.bash
ros2 run hw3_1 sub
```
10. Repeat for hw3_2 pub
```bash
source install/setup.bash
ros2 run hw3_2 pub
```
11. Repeat for hw3_2 sub
```bash
source install/setup.bash
ros2 run hw3_2 sub
```
