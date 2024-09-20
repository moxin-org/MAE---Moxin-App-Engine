
# **MoFA**

*With MoXin in the heart, Play **MoFa** magic, Show Moly to the world.*

## What is MoFa?

**MoFa** stands for **Mo**xin **F**ramework for **A**gent Composition.

MoFa is a software framework that builds AI agents through composition. With MoFa, AI agents can be created using templates, combined in a stackable manner to form more powerful "super agents."

## Why MoFa?

Using MoFa to build agents has several key benefits:

1. **Modularity**: Modular agent templates and services, with simple configuration and easy-to-use interfaces between modules.
2. **Clarity**: Build complex systems using a "LEGO-like" combination of logical blocks.
3. **Composability**: Agents can connect to services for enhanced capabilities or to other agents for expanded functionality.
4. **Simplicity**: Constructing complex agents is a zero-code process of combining different modules.
5. **High Performance**: Agent data streams run in a high-performance, low-latency distributed AI and robotics environment called **DORA-RS**, outperforming Python-based computational environments.
6. **Diversity**: MoFa’s composable agents integrate various agent capabilities into powerful, complete super agents.
7. **Towards AI Operating Systems (AIOS)**: Inspired by Unix Philosophy, MoFa provides core services for planning, memory, actions, and Retrieval-Augmented Generation (RAG), building the foundation of an AI operating system.
8. **Enable Edge AI**: With MoFa, alongside MoXin (local large model inference) and MoLy (user interface for AI models and agents), the deployment of local AI agents becomes more open and democratic.

## Getting Started

### 1. Installation

1. Clone the repository and switch to the specified branch:

```sh
git clone <repository-url> && git checkout <branch-name>
```

**Example**:

```sh
git clone git@github.com:moxin-org/mofa.git && cd mofa && git checkout feature/mofa
```

2. Use Python 3.10 or higher:

If there are version conflicts, you can create a new environment with conda:

```sh
conda create -n py310 python=3.10.12 -y
```

3. Set up the project environment:

- Install the necessary dependencies:

```sh
cd python && pip3 install -r requirements.txt && pip3 install -e .
```

After installation, you can use the `mofa --help` command to check for CLI options.

4. Install Rust and DORA-RS:

Since DORA-RS is built on Rust, please visit the following link to install the Rust environment based on your operating system:

```sh
https://www.rust-lang.org/tools/install
```

### 2. Configuration

In the `examples` directory, we provide a few agent case studies. First, configure the `.yml` files under the `configs` folder for each agent. If you installed the node using pip, navigate to the `agent-hub` folder, find the relevant node, and modify its corresponding `.yml` file.

Here is an example of configuring the **OpenAI API**:

```yaml
MODEL:
  MODEL_API_KEY:  
  MODEL_NAME: gpt-4o-mini
  MODEL_MAX_TOKENS: 2048
```

You can also configure other models such as Ollama or Moxin’s open-source local models:

**Ollama Example:**

```yaml
MODEL:
  MODEL_API_KEY: ollama
  MODEL_NAME: qwen:14b
  MODEL_MAX_TOKENS: 2048
  MODEL_API_URL: http://192.168.0.1:11434
```

**Configuring RAG (Retrieval-Augmented Generation)**:

```yaml
RAG:
  RAG_ENABLE: false   # Whether to enable the RAG feature.
  MODULE_PATH: null  # If there is no local embedding model, you can pass null.
  RAG_MODEL_NAME: text-embedding-3-small  # If using an OpenAI embedding model, specify the OpenAI embedding model name here.
  COLLECTION_NAME: mofa # The name of the collection in the vector database; use the default value.
  IS_UPLOAD_FILE: true # Whether to upload files to the vector database; set to true to upload, or false to skip.
  CHROMA_PATH: ./data/output/chroma # Path where the local vector database is saved.
  FILES_PATH: # Paths of the files to be uploaded; you can configure multiple files at once.
    - ./data/output/arxiv_papers
  ENCODING: utf-8  # The file encoding format.
  CHUNK_SIZE: 256 # The size of each text chunk; 256 is the recommended default value.
  RAG_SEARCH_NUM: 2 # The larger the value, the more results returned by the RAG search; however, ensure the total tokens do not exceed the LLM's token limit.
```

### 3. Running MoFa

You can run MoFa agents via the command line.

#### Common Commands

**List available agents**:

```bash
mofa agent-list
```

**Run an agent**:

```bash
mofa run --agent-name reasoner
```

**Exit the agent**:

To stop the agent, simply type `exit` or `quit`.

**Q: What should I do if Dora freezes?**

**A:** Use the following command with `sudo` to kill the process:

```bash
pkill dora
```

This will terminate all Dora-related processes, so use it with caution.

## Features

### MoFa Design Patterns for AI Agents

AI agents can follow various design patterns, such as:

- **LLM Inference**: The simplest agent, leveraging a large language model to generate responses based on user prompts.
- **Customized Prompting**: Creating agents by customizing system prompts for language models.
- **Reflection**: Agents that review and adjust their outputs.
- **Actor (Tool Use)**: Agents capable of using external tools, generating code, calling APIs, and performing web searches.
- **ReAct**: Combining reflection and tool use to improve output quality.
- **Multi-Agent Collaboration**: Multiple agents working together to solve complex tasks as a team.

MoFa allows you to combine these simple patterns into more complex "super agents" using modular templates.

### Agent Kernel Services

Similar to how traditional operating systems provide core services to applications, MoFa provides memory, planning, RAG, and action services to agents, allowing users to tailor these capabilities to their needs.

### Agent Composition

Composition in MoFa allows agents to be combined like LEGO blocks, creating powerful and complex agents without modifying the individual components. This modular approach ensures reversibility and scalability.

### Dataflow Driven Design

MoFa uses a dataflow-driven approach, emphasizing the movement of data between tasks rather than complex workflows. This simplifies managing and debugging agents.

## Examples

You can find MoFa examples in the [examples](python/examples) directory:

1. **simplexity_ai**: A search case inspired by Perplexity.ai, using Google Search API.
2. **agent_fight**: An agent that evaluates and scores reports generated by other agents competing on the same task.
3. **arxiv_research**: A multi-agent system that searches the arXiv database, downloads papers, and generates research reports.
4. **query_assistant**: A simple agent that answers user questions.

---

