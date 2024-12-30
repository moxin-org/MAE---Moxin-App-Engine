# 智能体简介

AI Agent已经是一个在人工智能领域人尽皆知的概念了。其相关技术迅速发展。关于它的定义尚未成埃落定。我们来看一看不同机构对智能体的定义。

Amazon （https://aws.amazon.com/what-is/ai-agents/）: 

很多人把Agent一词翻译成为代理。亚马逊则将AI Agent称为人工智能座席。

人工智能座席是一种软件程序，它可以与环境互动，收集数据，并利用数据执行自决任务，以实现预定目标。人类设定目标，但人工智能座席会独立选择实现这些目标所需的最佳行动。例如，联络中心的人工智能座席需要解决客户的疑问。该座席会自动向客户提出不同的问题，查找内部文件中的信息，并给出解决方案。根据客户的回复，它可以决定是自己解决查询，还是将查询转给人工处理。

人工智能座席是基于理性的座席。它们根据自己的感知和数据做出理性决策，以产生最佳性能和结果。人工智能座席通过物理或软件接口感知环境。

例如，机器人座席会收集传感器数据，聊天机器人会将客户的询问作为输入。然后，人工智能座席采用这些数据做出可靠的决定。它通过分析收集到的数据来预测支持预定目标的最佳结果。人工智能座席还利用这些结果制定下一步应采取的行动。例如，自动驾驶汽车会根据来自多个传感器的数据绕过道路上的障碍物。

------

IBM （https://www.ibm.com/think/topics/ai-agents）: 

AI Agent是指一种能够自主代表用户或其他系统执行任务的系统或程序，它通过设计工作流程并利用可用工具来完成任务。

AI 代理的功能远不止自然语言处理，还包括决策制定、问题解决、与外部环境交互以及执行操作。

这些代理可以部署在各种应用中，解决企业环境中的复杂任务，从软件设计、IT 自动化到代码生成工具和对话助手等领域。它们利用大语言模型（LLM）的先进自然语言处理技术，逐步理解并响应用户输入，并根据需要调用外部工具。

> 

------

Microsoft （https://learn.microsoft.com/en-us/azure/cosmos-db/ai-agents）：

人工智能（AI）代理旨在为用户执行特定任务、回答问题并自动化流程。这些代理的复杂性差异很大，从简单的聊天机器人、助手，到能够自主运行复杂工作流程的高级 AI 助手（数字或机器人系统形式）。

与独立的大型语言模型（LLM）或基于规则的软件/硬件系统不同，AI 代理具备以下共同特征：

- 规划：AI 代理能够计划和排序行动以实现特定目标。LLM 的集成革命性地提升了其规划能力。
- 工具使用：高级 AI 代理可以使用各种工具，如代码执行、搜索和计算功能，以有效完成任务。AI 代理通常通过函数调用使用工具。
- 感知：AI 代理能够感知并处理来自环境的信息，使其更具互动性和上下文感知能力。这些信息包括视觉、听觉及其他感官数据。
- 记忆：AI 代理具备记住过去交互（工具使用和感知）和行为（工具使用和规划）的能力。他们存储这些经验，甚至进行自我反思，以指导未来的行动。此记忆功能使代理的性能随时间的推移保持连续性并得到改进。

Andrew Ng的定义更加具体一些，也跟接近于程序员的语言。他用了Workflow, design pattern等与程序员们相对亲切的语言来定义：

他提出，使用**Agentic Workflow**的概念更接近于实际一些。而Agentic Workflow区别于一般Workflow的特点是，它能够自主地“思考”和迭代改进它的答案。

![Image](https://mmbiz.qpic.cn/mmbiz_png/ibqbukt6PTv4licZoCqibZCsgEHlKW5PM5D8Zl1Dfzv5jntDOlTrhv5WgCex9YS5tRVemf6sc9jBRVzicZvacNZbdg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

他认为，Agentic Workflow往往有四种设计模式。反思，工具使用，规划和多智能体写作。

![Image](https://mmbiz.qpic.cn/mmbiz_jpg/ibqbukt6PTv4licZoCqibZCsgEHlKW5PM5DbWPH0nRy98ic0KesqWJSriaHEpo0gDa30BjXPvhoG21DjD1bEQXibkd6w/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
