ROS2 创建工作空间
========================
-----------------------------------------
**创建一个空白的工作空间**
 ```
 mkdir -p ~/dev_ws/src
 cd ~/dev_ws/src
 ```
添加代码
然后进行编译 ： 初始化ROS 2工作空间，并编译所有默认的ROS 2软件包
```
colcon build --symlink-install
```
编译之后，需要配置环境变量  
环境变量配置，环境变量的路径在 **/install/local_setup.sh**  
指令(注意更改路径)：
```
source install/local_setup.sh
```
或者将该指令放在.bashrc文件中


**功能包**
### 创建功能包
指令  
**ros2 pkg create --build-type <build-type><package_name>**  
示例：
```
cd ~/dev_ws/src
ros2 pkg create --build-type ament_cmake xuanlearning_pkg    # C++版本
ros2 pkg create --build-type ament_python xuanlearning_pkg   # python版本
```
编译功能包
```
cd ~/dev_ws/src
colon build                                                 # 注意，在根目录下执行
source install/local_setup.sh
```

### **创建功能包的结构**
**创建的一个C++版本空白的功能包包含：**
1. CmakeLists.txt    # 编译规则
2. package.xml       # 功能包的基本信息 以及 声明功能包的依赖项

**创建的一个python版本空白的功能包包含：**
1. package.xml       # 功能包的基本信息 以及 声明功能包的依赖项
3. setup.py          # 程序入口程序点的描述，将python的可执行文件的配置
2. setup.cfg         # 功能包的信息 不需要修改
