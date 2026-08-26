# TAGLINE

Charm 出品的命令行 AI 助手

# TLDR

**问一个一次性问题**

```mods "[explain what SIGPIPE does]"```

**把文件内容管道输入到提示词**

```cat [file.py] | mods "[review this code for bugs]"```

**选择特定模型**

```mods -m [gpt-4o] "[summarise this]"```

**继续最近一次对话**

```mods -C "[and how would I test that?]"```

**恢复命名过的对话**

```mods -c [refactor] "[next step]"```

**以 Markdown 格式输出响应**

```mods -f "[write release notes from these commits]"```

**列出已保存的对话**

```mods -l```

**应用自定义角色/系统提示词**

```mods --role [shell] "[find large files in /var]"```

# SYNOPSIS

**mods** [_options_] [_prompt_]

# PARAMETERS

_PROMPT_
> 传给模型的文本。与从 STDIN 读入的数据合并。

**-m**, **--model** _NAME_
> 使用指定模型（例如 `gpt-4o`、`claude-3-5-sonnet` 或本地 Ollama 模型）。

**-M**, **--ask-model**
> 以交互方式提示选择模型。

**-f**, **--format**
> 要求模型输出带格式的（Markdown）内容，并在终端中渲染。

**--format-as** _FORMAT_
> 指定输出格式（例如 `markdown`、`json`）。

**-r**, **--raw**
> 打印原始、不带格式的响应。

**-q**, **--quiet**
> 抑制错误以外的输出。

**-P**, **--prompt**
> 在响应中包含来自命令参数和 STDIN 的提示词。

**-p**, **--prompt-args**
> 在响应中包含 CLI 的提示词参数。

**--max-tokens** _N_
> 限制响应长度。

**--no-limit**
> 不限制响应长度。

**--word-wrap** _WIDTH_
> 在给定列宽处折行（默认：80）。

**-t**, **--title** _NAME_
> 为当前对话命名以便日后检索。

**-l**, **--list**
> 列出已保存的对话。

**-c**, **--continue** _NAME_
> 按名称恢复已保存的对话。

**-C**, **--continue-last**
> 恢复最近一次对话。

**-s**, **--show** _NAME_
> 打印一个已保存的对话。

**--no-cache**
> 不将对话持久化到缓存。

**--role** _NAME_
> 应用配置中定义的自定义角色/系统提示词。

**--temp** _FLOAT_
> 采样温度。

**--topp** _FLOAT_, **--topk** _INT_
> Top-p / top-k 采样参数。

**--theme** _NAME_
> UI 主题（`charm`、`catppuccin`、`dracula`、`base16`）。

**-x**, **--http-proxy** _URL_
> 通过 HTTP 代理路由请求。

**--settings**
> 在 `$EDITOR` 中打开设置文件。

# DESCRIPTION

**mods** 是一个命令行 AI 伴侣，它把 STDIN 和参数组装成提示词，发送给配置好的 LLM，并把响应流式地回显到终端。它支持 OpenAI、Anthropic、Cohere、Groq、Google Gemini、Azure 以及 Ollama 和 LocalAI 等本地提供商，可通过 **--model** 按请求选择，或在 YAML 配置中指定。

对话会缓存到磁盘，因此可以按名称恢复或从上一轮继续；启用 **--format** 后，经由 Glamour 渲染的 Markdown 回复能以语法高亮和标题的形式展示。

# CAVEATS

需要为所选提供商配置 API 密钥（或本地端点）；商业提供商按 token 计费。除非使用 **--no-cache**，否则从 shell 发送的提示词会以明文形式存储在缓存目录中。

截至 **2026 年 3 月**，上游项目已被归档；Charm 推荐 **Crush** 作为其继任者，不过现有的 mods 安装仍可继续使用。

# HISTORY

**mods** 由 **Charm** 创建，是其终端工具套件的一员（与 gum、glow、charm 并列）。它于 2026 年 3 月被归档，由 Charm 较新的 Crush CLI 取代。

# INSTALL

```brew: brew install mods```

```nix: nix profile install nixpkgs#mods```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[llm](/man/llm)(1), [ollama](/man/ollama)(1), [glow](/man/glow)(1), [gum](/man/gum)(1), [charm](/man/charm)(1)
