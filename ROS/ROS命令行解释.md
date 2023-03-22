ROS2 命令行解释
========================
-----------------------------------------
| 参数 Parameter    | 功能  Function          |
| :--------------- | :----------------- :    |
|ros2 run       | 运行ROS 2软件包中的节点       |
|ros2 topic     | 查看ROS 2话题的信息           |
|ros2 node      | 查看ROS 2节点的信息           |
|ros2 launch    | 启动ROS 2软件包中的多个节点    |
|ros2 param     | 管理ROS 2参数                |
|ros2 service   | 查看ROS 2服务的信息           |
|ros2 action    | 查看ROS 2动作的信息           |
|ros2 bag       | 录制和回放ROS 2话题数据        |
|ros2 doctor    | 诊断ROS 2环境是否配置正确      |

-----------------------------------------

## **节点**
    | 参数 Parameter    | 功能  Function          |
    | :--------------- | :-----------------:      |
    | list       |输出节点列表                     |
    | info       |输出节点信息                     |

ros2 run：运行 ROS2 软件包中的节点
```
ros2 run turtlesim turtlesim_node
```
该命令运行了 turtlesim 功能包中 turtlesim_node 仿真器的节点

```
ros2 run turtlesim turtle_teleop_key
```
该命令运行了 turtlesim 功能包中 turtle_teleop_key 键盘控制的节点

```
ros2 node list
```
该命令运行了 查看ROS2系统中正在运行的节点清单 打印出来
```
ros2 node info +/node
```
该命令运行了 查看节点信息
-----------------------------------------

## **话题**

```
ros2 topic +参数 + /topic
```

    | 参数 Parameter    | 功能  Function      |
    | :--------------- | :-----------------: |
    | bw    |    显示主题(话题)使用的带宽      |
    | delay |    从标题中的时间戳显示主题的延迟  |
    | echo  |    输出一个主题的信息            |
    | find  |    输出一个给定类型的可用主题的列表 |
    | hz    |    打印平均发布率到屏幕上         |
    | info  |    打印关于一个主题的信息         |
    | list  |    输出可用主题的列表            |
    | pub   |    向主题发布消息                |
    | type  |    打印一个主题的类型            |   

```
ros2 topic pub --rate 1 /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```
功能：
向话题发布一个消息，消息的信息内容是控制小乌龟的线速度和角速度
参数：
rate 1           ->  消息发布频率 1Hz
/turtle1/cmd_vel ->  针对turtle1 速度控制的指令
geometry_msgs/msg/Twist  -> 发布的话题消息；类似于数据结构
linear ； angular ->  数据结构的两个参数

-----------------------------------------
## **服务**

```
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: 'XU'}"
```
功能：
调用一个spawn服务；在特定位置产生一个新的小乌龟，命名为xu 
参数：
spawn -> 服务名称
turtlesim/srv/Spawn -> 数据结构
x,y,theta -> 位置及角度
name -> 命名
 
 
 
 
 


-----------------------------------------
## **录制控制命令**

    | 参数 Parameter    | 功能  Function          |
    | :--------------- | :-----------------:      |
    |convert     |给出一个bag，写出一个具有不同设置的新bag   （转换）     |
    |info        |在屏幕上打印一个bag的信息                            |
    |list        |在屏幕上打印关于可用插件的信息                        |
    |play        |从一个bag中回放ROS数据                             |
    |record      |记录ROS数据到一个bag中                             |
    |reindex     |重构一个bag的元数据文件                             |
 

    Given an input bag, write out a new bag with different settings
    Print information about a bag to the screen
    Print information about available plugins to the screen
    Play back ROS data from a bag
    Record ROS data to a bag
    Reconstruct metadata file for a bag

```ROS2
ros2 bag record /turtle1/cmd_vel$ ros2 bag play rosbag2_2022_04_11-17_35_40/rosbag2_2022_04_11-17_35_40_0.db3
```
