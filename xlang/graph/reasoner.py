import json
import os

from mofa.utils.envs.util import init_proxy_env

from xMind import xMind
from mofa.kernel.utils.util import load_agent_config
from mofa.run.run_agent import  run_dspy_or_crewai_agent
from mofa.utils.files.dir import get_relative_path
from mem0 import Memory
from mofa.utils.files.read import read_yaml


@xMind.Agent(inputs=[{"name":"input"}],name="ReasonerAgent")
def ReasonerAgent(owner):
	inputData = owner.waitInput()
	if inputData[0] == xMind.Ok:
		data = inputData[2]
		inputs = load_agent_config(r"D:\project\mae_new\xMind\Scripts\configs\reasoner_agent.yml")
		inputs["task"] = data
		agent_result = run_dspy_or_crewai_agent(agent_config=inputs)
		xMind.log("AgentFirst LLM->: ",agent_result)

@xMind.Action(outputs=[{"name":"output"}],name="ActionTask")
def ActionTask(owner):

	prompt = input("Input a prompt to ask AgentFirst:")
	if prompt == '!quit':
		xMind.Stop()
	else:
		xMind.log("Your Prompt:",prompt)
		owner.pushToOutput(0,prompt)


graph = xMind.Graph()
graph.addNode(ActionTask)
graph.addNode(ReasonerAgent)

graph.connect("ActionTask","ReasonerAgent")
graph.run()

xMind.MainLoop()

xMind.log("Done")