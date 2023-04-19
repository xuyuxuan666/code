linux常用指令
====================================
```linux
ls
cd
cd -                        # 返回上一个路径
mkdir <文件夹名>
touch <文件名>
```

``` 删除
rm [参数] <文件名>
```
**参数说明：**  
| 参数              | 解释         |
|:---------------:  | :-----:    
-f      -force      | 忽略不存在的文件，强制删除，无任何提示  
-i     -interactive | 进行交互式删除  
-r/-R    -recursive | 递归式地删除列出的目录下的所有  
-V       -verbose   | 详细显示进行的步骤  

**命令行查看版本：**
```命令行查看版本
cat /etc/issue    # 查看Ubuntu系统版本
nvcc --version    # 查看cuda版本
nvidia-smi        # 查看GPU
```
**python查看版本**
```
import torch
import tensorrt as trt
print(trt.__version__)
print(torch.backends.cudnn.version())
print(torch.version.cuda)
print(torch.__version__)
```

