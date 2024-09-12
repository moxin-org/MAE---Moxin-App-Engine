# Agent Fight

## 1. Overview
This tool is designed to compare and evaluate the results of two agents and/or LLMs. It provides scoring and assessment across various dimensions for each agent's results.

## 2. Use Cases
Evaluate the performance of different agents in competitions by assessing their results.

## 3. Configuration
To modify the `Prompt` and other settings, update the `content_evaluation_agent.yml` file, located in the `content-evaluation` directory under `agent-hub`.

## 4. Running AgnetFight

### Method 1: Using Dora-rs Commands

1. Install the MoFA project package.
2. Run the following commands:
   ```bash
   dora up && dora build agent_fight_dataflow.yml && dora start reasoner_dataflow.yml
3. Open another terminal and run multiple-terminal-input. Enter the following three parameters:
   - **primary_data**: The result of the first agent (provide an absolute path to a Markdown file).
   - **second_data**: The result of the second agent (provide an absolute path to a Markdown file).
   - **source_task**: The task that generated the agent results. For example, both "primary_data" and "second_data" are generated from the same task.
