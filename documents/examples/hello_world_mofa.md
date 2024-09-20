# 基于 MoFA 的 Hello World 智能体开发
## 步骤 1：安装 MoFA 环境和 xMind

### 1. 安装必要的依赖

```bash
sudo apt update
sudo apt install -y git build-essential cmake uuid-dev libssl-dev python3-dev make
```

### 2. 克隆 xMind 仓库

```bash
git clone https://github.com/xlang-foundation/xMind.git
cd xMind/ThirdParty
```

### 3. 克隆 xlang 依赖

```bash
git clone https://github.com/xlang-foundation/xlang.git
```

### 4. 构建 xMind

```bash
cd ..
mkdir out && cd out
cmake .. && make
```

### 5. 复制 `xMind.py` 脚本到你创建的Hello World目录下

```bash
cp ../Scripts/xMind.py Hello World Path
```

## 步骤 2：获取 Reasoner MoFA 模版
原始的MoFA [Reasoner](../../xlang/graph/reasoner.py)模版代码

该模版实现了一个基于 xMind 框架的代理系统，包含两个主要组件：`ReasonerAgent` 和 `ActionTask`。

### 1. 导入所需库

```python
import json
import os

from mofa.utils.envs.util import init_proxy_env
from xMind import xMind
from mofa.kernel.utils.util import load_agent_config
from mofa.run.run_agent import run_dspy_or_crewai_agent
from mofa.utils.files.dir import get_relative_path
from mem0 import Memory
from mofa.utils.files.read import read_yaml
```

- 导入用于环境初始化、配置加载、代理运行等功能的模块。

### 2. 定义 `ReasonerAgent`

```python
@xMind.Agent(inputs=[{"name":"input"}], name="ReasonerAgent")
def ReasonerAgent(owner):
    inputData = owner.waitInput()
    if inputData[0] == xMind.Ok:
        data = inputData[2]
        inputs = load_agent_config(r"D:\project\mae_new\xMind\Scripts\configs\reasoner_agent.yml")
        inputs["task"] = data
        agent_result = run_dspy_or_crewai_agent(agent_config=inputs)
        xMind.log("AgentFirst LLM->: ", agent_result)
```

- **功能**：接收并处理输入数据。
- **流程**：
  1. 等待输入数据。
  2. 检查输入是否有效。
  3. 从配置文件加载代理配置。
  4. 将数据作为任务传递给代理并执行。
  5. 记录执行结果。

### 3. 定义 `ActionTask`

```python
@xMind.Action(outputs=[{"name":"output"}], name="ActionTask")
def ActionTask(owner):
    prompt = input("请输入要发送给 AgentFirst 的提示:")
    if prompt == '!quit':
        xMind.Stop()
    else:
        xMind.log("您的提示:", prompt)
        owner.pushToOutput(0, prompt)
```

- **功能**：获取用户输入并将其推送到输出。
- **流程**：
  1. 获取用户输入。
  2. 如果输入为 `'!quit'`，则停止程序。
  3. 否则，记录日志并将输入推送到输出。

### 4. 创建图形结构并运行

```python
graph = xMind.Graph()
graph.addNode(ActionTask)
graph.addNode(ReasonerAgent)

graph.connect("ActionTask", "ReasonerAgent")
graph.run()

xMind.MainLoop()

xMind.log("完成")
```

- **步骤**：
  1. 创建 `Graph` 对象。
  2. 添加 `ActionTask` 和 `ReasonerAgent` 节点。
  3. 连接两个节点，定义数据流向。
  4. 启动图形执行和主循环。
  5. 程序结束时记录日志。

## 步骤 3：定制 Reasoner MoFA 模版，创建 Hello World Agent

- **配置定制**：
  - 根据 [hello_world_dora](hello_world_dora.md) 的逻辑定制 `agent.yml` 文件。
  - 确保配置文件中的参数符合 Hello World Agent 的需求。

## 步骤 4：运行 AgentFlow 图

### 1. 命令行运行

在终端中执行以下命令启动 Hello World Agent：

```bash
python3 hello_world.py
```

### 2. Web 运行

（根据具体需求和配置，补充相关 Web 运行步骤）

---

