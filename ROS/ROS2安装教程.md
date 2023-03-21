ROS2 Ubuntu22.04 安装教程
========================
-----------------------------------------
## **步骤 1：设置区域设置**

检查您的系统是否支持 UTF-8。为此，请在终端上运行
```terminal
locale
```
以下命令输出，则一切就绪

![](https://github.com/xuyuxuan666/code/blob/main/ROS/%E5%9B%BE%E7%89%87%E5%8F%8A%E7%BC%93%E5%AD%98/ROS.png)

如果您的系统不支持 UTF-8，则通过运行以下命令来安装语言环境：

```terminal
sudo apt update && sudo apt install locales
```


安装后，使用以下命令生成 UTF-8 语言环境。
```terminal
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
```

然后定义并导出环境变量
```terminal
export LANG=en_US.UTF-8
```

此时，您的系统应提供对 UTF-8 语言环境的支持。您可以使用 locale 命令验证现在是否支持 UTF-8

## **第 2 步：将官方 ROS 2 Humble 存储库添加到 Ubuntu**
将官方 ROS2 Humble 存储库添加到您的系统中
```terminal
sudo apt install software-properties-common curl gnupg lsb-release
```
安装 ROS 2 Humble 需要您为系统启用 Ubuntu Universe 存储库。Universe 存储库是一个标准存储库，
要将 Universe 存储库添加到您的系统，请运行以下命令：
```terminal
sudo add-apt-repository universe
```
更新列表包

```terminal
sudo apt update
```

添加 ROS 提供的公网 GPG 密钥
```terminal
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```
添加 GPG 密钥后，使用以下命令将 ROS 2 存储库添加到 /etc/apt/sources.list.d/ 目录中

```terminal
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```
## **步骤 3：更新ROS 3包索引**
设置好 ROS 存储库后，更新 APT 存储库缓存
```terminal
sudo apt update
sudo apt upgrade
```

## **步骤 4：在Ubuntu上安装ROS2**
```terminal
sudo apt install ros-humble-desktop
```

## **步骤 5：设置ROS2**

安装完成后，您需要获取安装文件。为此，请运行以下命令
```terminal
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

## **步骤 6：验证ROS2**
要测试 ROS API 是否正常工作，请导航到 /opt/ros/humble/lib/demo_nodes_cpp/ 目录
```terminal
cd /opt/ros/humble/lib/demo_nodes_cpp/
```
按如下方式运行C++

```terminal
ros2 run demo_nodes_cpp talker
```

或者，切换到 /opt/ros/humble/lib/demo_nodes_py/ 目录
```terminal
cd /opt/ros/humble/lib/demo_nodes_py/
```
并运行 Python 以使用以下命令检查 python apis 是否正常工作
```terminal
ros2 run demo_nodes_py listener
```