# Agent Fight  

## 1. 功能说明
用于对比和评估两个Agent的结果.对每个agent结果在不同的维度上面进行打分和评估

## 2. 使用场景
在比赛中对不同的Agent的结果能力进行评估

## 3. 配置方法
通过更改`agent-hub`下面的`content-evaluation`目录下面的`content_evaluation_agent.yml`模版里的配置信息来对`Prompt`等进行修改

## 4. 运行Agent

### 方法一：在Dora-rs命令里运行：

1. 安装MoFA项目包
2. `dora up && dora build  reasoner_dataflow.yml && dora start reasoner_dataflow.yml`
3. 启动另外一个命令端,在另外一个命令端运行 `multiple-terminal-input`.然后输入需要输入三个参数
   - **primary_data** : 第一个agent的结果(可以传输一个markdown的文件路径,要求是绝对路径)
   - **second_data** : 第二个agent的结果(可以传输一个markdown的文件路径,要求是绝对路径)
   - **comparison_task** : 生成agent结果的任务. 例如: "primary_data"和"second_data"都是通过同一个任务去生成的. 
 
