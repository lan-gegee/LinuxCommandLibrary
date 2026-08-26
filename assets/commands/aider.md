# TAGLINE

终端里的 AI 结对编程

# TLDR

**启动** aider 并加载文件

```aider [file1.py] [file2.py]```

使用**指定模型**

```aider --model [gpt-4] [file.py]```

以**架构师模式**启动

```aider --architect [file.py]```

启用**自动提交**

```aider --auto-commits [file.py]```

使用**本地 Ollama** 模型

```aider --model ollama/[llama2] [file.py]```

# SYNOPSIS

**aider** [_options_] [_files_...]

# DESCRIPTION

**aider** 是一个在你的终端中工作的 AI 结对编程助手。它可以让你就代码与 AI 模型（GPT-4、Claude、Ollama 模型等）对话，AI 能够直接编辑你的源文件。

该工具与 git 集成，可自动提交更改，并能理解你整个代码库的上下文。你可以将文件加入对话、提出问题、请求修改，然后看着 AI 实现这些修改。

# PARAMETERS

**--model** _name_
> 要使用的 AI 模型（gpt-4、gpt-3.5-turbo、claude-3-opus 等）

**--architect**
> 使用架构师模式：由架构师模型提出修改方案，再由单独的编辑器模型实施文件编辑

**--edit-format** _format_
> 编辑格式：diff、whole、diff-fenced

**--auto-commits**
> 自动提交 AI 的更改（默认启用）

**--no-auto-commits**
> 禁用自动提交

**--dark-mode**
> 使用适合深色终端背景的颜色

**--light-mode**
> 使用适合浅色终端背景的颜色

**--map-tokens** _n_
> 仓库映射的最大 token 数

**--no-git**
> 禁用 git 集成

**--yes**
> 自动确认所有提示

**--message** _text_
> 发送一条消息后退出

# CONFIGURATION

**.aider.conf.yml**
> 每个项目的配置文件，用于默认选项、模型选择和行为设置。

**.aiderignore**
> 从仓库映射中排除的文件和目录，使用 .gitignore 语法。

# CAVEATS

云模型需要 API 密钥（OPENAI_API_KEY、ANTHROPIC_API_KEY 等）。对于大型代码库，token 用量可能相当可观。接受 AI 生成的更改前请先审查。

# HISTORY

**aider** 由 Paul Gauthier 创建并于 **2023** 年发布。它的设计目标是利用大语言模型进行实用的代码编辑，并随着新 AI 模型的发布快速演进。

# INSTALL

```brew: brew install aider```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[git](/man/git)(1), [gh](/man/gh)(1), [copilot](/man/copilot)(1)
