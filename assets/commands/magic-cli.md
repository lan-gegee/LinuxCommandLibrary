# TAGLINE

用于建议和搜索 shell 命令的 LLM 助手

# TLDR

从自然语言提示词**建议**命令

```magic-cli suggest "[Resize image to 300x300 with ffmpeg]"```

以语义方式**搜索** shell 历史

```magic-cli search "[zellij attach]"```

让智能体**弄清**多步骤任务的做法

```magic-cli ask "[Set up the dev environment from the README]"```

**配置** LLM 提供方

```magic-cli config set llm [ollama]```

**列出**配置

```magic-cli config list```

# SYNOPSIS

**magic-cli** *command* [*args*]

# DESCRIPTION

**magic-cli** 利用大语言模型在 shell 中提供帮助：**suggest** 将粗略的意图转化为具体命令，**search** 通过嵌入向量在你的历史记录中查找相似命令，**ask** 则以交互方式朝着目标推进（可能会请求运行一些命令来获取上下文）。视版本而定，提供方包括 Ollama（本地）、OpenAI 和 Anthropic。

配置文件：**~/.config/magic_cli/config.json**（通过 **magic-cli config** 管理）。项目尚处于早期阶段——请预期会有破坏性变更。

# PARAMETERS

**suggest** *PROMPT*

> 为所描述的任务提出一条命令。

**search** *PROMPT*

> 对 shell 历史进行语义搜索（实验性；历史记录很大时，远程嵌入的开销可能较高）。

**ask** *PROMPT*

> 智能体式的命令生成，可选执行后续工具调用。

**config** **set**|**get**|**list**|**reset**|**path**

> 管理配置（**llm**、Ollama 的 base URL/模型、OpenAI 设置等）。

# CAVEATS

切勿盲目执行建议的命令——先检查是否含有破坏性标志。云端 LLM 会将提示词（可能还有部分历史片段）发送到本机之外。项目仍处于早期开发阶段。

# SEE ALSO

[tldr](/man/tldr)(1), [navi](/man/navi)(1), [sgpt](/man/sgpt)(1)

# RESOURCES

```[Source code](https://github.com/guywaldman/magic-cli)```

```[Homepage](https://guywaldman.com/posts/introducing-magic-cli)```

<!-- verified: 2026-07-19 -->
