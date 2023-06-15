Linux 快捷键
====================================
## **常用快捷键**
```
Ctrl + Alt + T              # 打开终端
Ctrl + Shift +T             # 在同一窗口下打开终端
Ctrl + H                    # 打开隐藏文件
Ctrl + D                    # 关闭当前终端
Ctrl + C                    # 中断正在运行的命令或进程
Ctrl + R                    # 在历史命令中搜索指定字符串
Ctrl + A                    # 将光标移动到命令行的开头。
Ctrl + E                    # 将光标移动到命令行的结尾
Ctrl + L                    # 清空终端屏幕
Tab                         # 自动补全命令或文件名
```

## **常用命令行**
### 路径、目录相关
```
cd                          # 切换路径目录空间
cd -                        # 返回上一个路径
cd ~                        # 切换到home目录
cd ..                       # 切换到上级目录
pwd                         # 显示当前工作目录的绝对路径
ls                          # 列出当前目录下的文件和子目录
ls -a                       # 列出隐藏文件和目录
ls -l                       # 列出文件和目录的详细信息
```
### 创建、删除相关
```
touch                       # 创建空白文件
mkdir dirname               # 创建新目录
mkdir dir1 dir2 dir3        # 创建多个新目录
mkdir -p dir1/dir1.1        # 创建多级目录
rmdir -f dirname            # 强制删除目录
rmdir dir1 dir2 dir3        # 删除多个空目录
mv                          # 移动文件或目录
cp                          # 复制文件或目录
rm filename                 # 删除一个文件
rm file1 file2 file3        # 删除多个文件
rm -r dirname               # 删除一个目录
rm -i filename              # 提示用户确认删除
rm -f filename              # 强制删除文件
rm -rf dirname              # 强制删除目录
```
### 查看相关
```
df -h                       # 查看硬盘使用情况
free -m                     # 查看内存使用情况
ifcongfig  / ip addr        # 查看网络接口
netstat -aux                # 查看所有网络连接信息
dmesg | grep tty            # 查看串口连接情况
uname -a                    # 查看系统内核和版本信息
lsb_release -a              # 查看 Ubuntu 版本信息
cat /proc/cpuinfo           # 查看 CPU 信息
cat /proc/meminfo           # 查看内存信息
whoami                      # 查看当前登录用户
uptime                      # 查看系统负载
```
### 复制移动相关
```
cp file1 file2              # 复制名为 file1 的源文件到名为 file2 的目标文件中
cp file1 file2 file3 directory # 复制名为 file1、 file2 和  file3 的源文件到名为 directory 的目标目录中
mv old_filename new_filename    # 将名为 old_filename 的文件重命名为 new_filename
mv file1 file2 file3 directory  # 将名为 file1、file2 和 file3 的源文件移动到名为 directory 的目标目录中

```

### 显示输出相关
```
cat filename                # 显示一个文件的内容
echo "Hello, world!"        # 打印文本
echo $VAR                   # 打印变量
```
### 搜索查找相关
```
find /path/to/dir -name "filename"      # 查找指定名称的文件或目录
find /path/to/dir -type f               # 查找指定类型的文件
find /path/to/dir -type d               # 查找指定类型的目录
grep "text" filename                    # 在文件中查找指定文本
grep "text" file1 file2 file3           # 在多个文件中查找指定文本
grep -i "text" filename                 # 忽略大小写
```

### 权限相关
```
chmod user filename                     # 修改文件或目录的所有者
chmod -R mode directory                 # 递归修改文件或目录的权限
mode 可以是由 r、w、x 组成的字符串r 表示读取权限，w 表示写入权限，x 表示执行权限
777 读写执行
```

