
---

# 基于 MoFA 的 Hello World 智能体开发

## 1. 安装必要的依赖

### macOS 系统
1. 安装必要的依赖：
   ```bash
   brew install ossp-uuid
   brew install openssl
   brew install jpeg-turbo  # 可选，用于图像模块
   brew install python3      # 可选，用于 Python 库集成
   pip install numpy
   ```

### Ubuntu 系统
1. 更新包列表并安装必要的依赖：
   ```bash
   sudo apt update
   sudo apt install -y git build-essential cmake uuid-dev libssl-dev python3-dev make python3-pip
   ```

### Windows 系统
1. ##### 安装 Python，并确保在环境变量中可直接访问。
2. 安装 CMake，下载链接：[CMake 下载](https://cmake.org/download/)。
3. 安装 Visual Studio，下载链接：[Visual Studio 下载](https://visualstudio.microsoft.com/zh-hans/downloads/)。在安装过程中选择自定义安装，确保安装 C++ 桌面开发工具。
4. 使用 Visual Studio 打开 `xMind` 目录，点击 `xMind.exe`，然后选择 `生成` -> `重新生成`。
**Q&A&**:


##  在windows下正常的添加python到编译环境中

安装xlang的时候,如果是windows的话,请你先在cmd中尝试使用`python`,如果存在运行之后跳转到windows中的商城等乱七八糟的页面上.那么你需要按照以下的步骤进行修改
~~~
**打开【设置】，点【应用】。** **在【应用】中点【应用和功能】。** **单击【更多设置】-【应用执行别名】 然后找到带有Python的内容,之后关闭这个应用别名**。
~~~

## 2. 克隆 xMind 仓库
```bash
git clone https://github.com/xlang-foundation/xMind.git
cd xMind/ThirdParty
```

## 3. 克隆 xlang 依赖
```bash
git clone https://github.com/xlang-foundation/xlang.git
```

## 4. 构建 xMind
```bash
cd ..
mkdir out && cd out
cmake .. && make
```

## 5. 停止当前服务

### macOS 和 Ubuntu
1. 查看运行服务：
   ```bash
   lsof -i :9902
   ```
2. 停止服务（根据输出找到对应的 PID）：
   ```bash
   kill -9 <PID>
   ```

### Windows
直接关闭服务器服务窗口即可。

## 6. 相关网址
- 模型网址: [SiliconFlow](https://cloud.siliconflow.cn/)
- 项目网址: [xlang-foundation GitHub](https://github.com/xlang-foundation)

---

