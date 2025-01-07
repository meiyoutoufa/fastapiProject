
### conda 使用

```bash
# 查看帮助
conda
conda -h
conda --help

# 查看版本 
conda -V
conda –-version

# 查看所有的虚拟环境
conda env list
conda info -e
conda info --envs 

# 激活/关闭环境 
conda activate env_name # 激活环境
conda deactivate # 关闭环境

# clean清理
conda clean -h # 查看clean清理帮助
conda clean -p # 清理无用安装包
conda clean -t # 清理tar包
conda clean --all # 清理所有安装包及cache

# config指令
conda config -h # 查看config帮助
conda config --show-sources # 查看源
conda config --add channels + 要添加的源 # 添加源
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

conda config --remove channels + 要删除的源 # 删除源
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/

# create指令 
conda create -h # 查看帮助 

conda create -n env_name python=3.11.7 # 创建指定版本Python的环境
conda create -n env_name python  # 默认最新版本Python的环境
conda create -n env_name  # 创建一个空的环境

conda create -n robot1 --clone robot # 根据环境名克隆环境
conda create -p E:\Software\anaconda3\envs\ robot2 --clone robot # 根据环境路径克隆环境

# 查看环境配置信息
conda info 
conda info -h # 查看帮助

# 包管理 
# 查看包
conda list # 列出当前环境中已安装的包
conda list --reverse # 按顺序列出已安装的包
conda list ^p # 使用“^”列出所有以字母“p”开头的包
conda list --export > requirements.txt # 输出包列表到文件
conda search <package_name> # 搜索一个未安装的包在conda库中是否存在
conda search '*<search_term>*' # 搜索包含特定字符的包
conda search <channel>::<package_name> # 搜索特定通道中的包

# 安装包
conda install <package_name> # 在当前环境中安装包。
conda install --name <env_name> <package_name> # 在指定环境中安装包。
conda install <package_name>=<version> # 安装特定版本的包。
conda install --channel <channel_name> <package_name> # 从特定通道安装包。
conda install --force-reinstall <package_name> # 强制重新安装包。

# 删除包
conda remove <package_name> # 删除当前激活环境中的包
conda remove --name <env_name> <package_name> # 删除指定环境中的包

# 更新包
conda update <package_name> # 更新当前激活环境中的包
conda update --all # 更新当前环境中的所有包
conda update --all --name <env_name> # 更新指定环境中的所有包

# 升级conda（只能在base环境中升级）
conda update conda 

```


## 项目中操作
```bash
conda serach sqlmodel

conda install fastapi

## 解决PackagesNotFoundError：当前频道中无法获取以下包的解决方案,那么需要去 https://anaconda.org 网址，搜索包的其他channel
conda install conda-forge::sqlmodel

## 导出环境文件，导出当前 Conda 环境为 environment.yml 文件（这种需要后续部署也有conda中，如果在容器中部署，可以考虑直接使用pip）
conda env export > environment.yml

## 导出环境，生成 requirements.txt 文件
pip freeze > requirements.txt
## 原本requirements.txt文件中指向本地的路径 替换为版本号
pip list --format=freeze > ./requirements.txt

```


