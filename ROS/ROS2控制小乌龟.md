ROS2 命令行入门
========================
-----------------------------------------
## **节点**

运行海龟仿真节点
```ROS2
ros2 run turtlesim turtlesim_node
```
键盘控制节点
```ROS2
ros2 run turtlesim turtle_teleop_key
```

查看节点列表信息

```ROS2
ros2 node list
```
查看某一个节点信息
```ROS2
ros2 node info /turtlesim
```


## **话题**

查看话题列表
```ROS2
ros2 topic list
```

查看某一个话题中的消息数据

```ROS2
ros2 topic echo /turtle1/pose
```

想要控制海龟动起来，我们还可以直接通过命令行发布话题指令：

```ROS2
 ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```

## **服务**

```ROS2
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: ''}"
```


## **动作**
想要让海龟完成一个具体动作，比如转到指定角度，仿真器中提供的这个action可以帮上忙，通过命令行这样发送动作目标：
```ROS2
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "theta: 3"
```


## **录制控制命令**


```ROS2
ros2 bag record /turtle1/cmd_vel$ ros2 bag play rosbag2_2022_04_11-17_35_40/rosbag2_2022_04_11-17_35_40_0.db3
```
