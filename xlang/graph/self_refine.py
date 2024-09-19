
from xMind import xMind
from mofa.kernel.utils.util import load_agent_config
from mofa.run.run_agent import  run_dspy_or_crewai_agent

def load_dict_key(key_name:str,dict_data:dict):
	value = dict_data.get(key_name,None)
	return value

@xMind.Agent(inputs=[{"name":"input"}],name="WriterReportAgent",outputs=[{"name":"output"}])
def WriterReportAgent(owner):
	inputData = owner.waitInput()
	if inputData[0] == xMind.Ok:
		data = inputData[2]
		inputs = load_agent_config(r"D:\project\mae_new\xMind\Scripts\configs\reasoner_agent.yml")
		inputs["task"] = data
		agent_result = run_dspy_or_crewai_agent(agent_config=inputs)
		xMind.log("AgentFirst LLM->: ",agent_result)
		owner.pushToOutput(0,{"writer_report_result":agent_result,"search_task":data,'local_iterations':1})

@xMind.Agent(inputs=[{"name":"data"}],name="FeedBackeAgent",)
def FeedBackeAgent(owner):
	inputData = owner.waitInput()
	if inputData[0] == xMind.Ok:
		data = inputData[2]

		inputs = load_agent_config(r"D:\project\mae_new\xMind\Scripts\configs\feedback_agent.yml")
		inputs["task"] = data.get("search_task")
		inputs["context"] = data.get("writer_report_result")
		agent_result = run_dspy_or_crewai_agent(agent_config=inputs)
		xMind.log("---------------------------\n")

		xMind.log("FeedBackeAgent LLM->: ",agent_result)
		data.update({"feedback_result":agent_result})
		owner.pushToOutput(0,data)

@xMind.Agent(inputs=[{"name":"data"}],name="RefineAgent",)
def RefineAgent(owner):
	inputData = owner.waitInput()
	if inputData[0] == xMind.Ok:
		data = inputData[2]

		inputs = load_agent_config(r"D:\project\mae_new\xMind\Scripts\configs\refinement_agent.yml")

		inputs['input_fields'] = {'search_task_suggestion': data.get("feedback_result"), 'search_task': data.get("search_task"),
								  'task_result': data.get("writer_report_result")}
		agent_result = run_dspy_or_crewai_agent(agent_config=inputs)
		xMind.log("---------------------------\n")

		xMind.log("RefineAgent LLM->: ",agent_result)
		data.update({"refine_result":agent_result})
		owner.pushToOutput(0,data)

@xMind.Agent(inputs=[{"name":"data"}],name="EvaluationAgent",)
def EvaluationAgent(owner):
	inputData = owner.waitInput()
	if inputData[0] == xMind.Ok:
		data = inputData[2]
		inputs = load_agent_config(r"D:\project\mae_new\xMind\Scripts\configs\evaluation_agent.yml")
		inputs['context'] = data.get("refine_result")
		inputs['task'] = data.get("search_task")
		max_iteration = inputs.get('max_iterations')
		agent_result = run_dspy_or_crewai_agent(agent_config=inputs)
		xMind.log("---------------------------\n")
		xMind.log("EvaluationAgent LLM->: ",agent_result)
		print("EvaluationAgent LLM->: ",agent_result)
		if 'Yes' in agent_result or 'yes' in agent_result:
			xMind.Stop()
		if data.get('local_iterations')<max_iteration :
			data['writer_report_result'] = data.get("refine_result")
			data['local_iterations'] +=1
			owner.pushToOutput(0,data)
		else:
			xMind.Stop()

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
graph.addNode(WriterReportAgent)
graph.addNode(FeedBackeAgent)
graph.addNode(RefineAgent)
graph.addNode(EvaluationAgent)

graph.connect("ActionTask","WriterReportAgent")

graph.connect("WriterReportAgent","FeedBackeAgent")
graph.connect("FeedBackeAgent","RefineAgent")
graph.connect("RefineAgent","EvaluationAgent")
graph.connect("EvaluationAgent","FeedBackeAgent")
graph.run()

xMind.MainLoop()

xMind.log("Done")