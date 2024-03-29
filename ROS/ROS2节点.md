ROS2 节点
========================
-----------------------------------------


## **节点面向过程的编程(不能模块化,了解)**

1. 编程接口初始话
2. 创建节点并初始化
3. 实现节点功能
4. 销毁节点并关闭接口

Hello world py代码
```
import rclpy                                     # ROS2 Python接口库
from rclpy.node import Node                      # ROS2 节点类
import time

def main(args=None):                             # ROS2节点主入口main函数
    rclpy.init(args=args)                        # ROS2 Python接口初始化
    node = Node("node_helloworld")               # 创建ROS2节点对象并进行初始化
    
    while rclpy.ok():                            # ROS2系统是否正常运行
        node.get_logger().info("Hello World")    # ROS2日志输出
        time.sleep(0.5)                          # 休眠控制循环时间
    
    node.destroy_node()                          # 销毁节点对象    
    rclpy.shutdown()                             # 关闭ROS2 Python接口
```
配置程序入口(python版本)：
```
    entry_points={     # 程序入口点
        'console_scripts': [
         'node_helloworld       = learning_node.node_helloworld:main',
         # 格式：'节点名称 = <功能包>.<文件名>:main',
        ],
```


在setup.py文件中

## **节点面向对象的编程(类)**

**什么是节点：**        
在ROS 2中，节点（Node）是一个可以相互通信的进程。每个节点都有一个唯一的名称，并且可以通过ROS 2的通信机制与其他节点进行通信。

节点可以发布（Publish）消息到主题（Topic）中，也可以订阅（Subscribe）主题以接收消息。此外，节点还可以提供（Provide）服务（Service）以响应请求，也可以调用（Call）其他节点提供的服务。

```
import rclpy                                     # ROS2 Python接口库
from rclpy.node import Node                      # ROS2 节点类
import time

"""
创建一个HelloWorld节点, 初始化时输出“hello world”日志
"""
class HelloWorldNode(Node):
    def __init__(self, name):
        super().__init__(name)                       # ROS2节点父类初始化
        while rclpy.ok():                            # ROS2系统是否正常运行
            self.get_logger().info("Hello World")    # ROS2日志输出
            time.sleep(0.5)                          # 休眠控制循环时间

def main(args=None):                                 # ROS2节点主入口main函数
    rclpy.init(args=args)                            # ROS2 Python接口初始化
    node = HelloWorldNode("node_helloworld_class")   # 创建ROS2节点对象并进行初始化
    node.destroy_node()                              # 销毁节点对象
    rclpy.shutdown()                                 # 关闭ROS2 Python接口
```
同样需要配置程序入口。