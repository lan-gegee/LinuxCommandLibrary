# TAGLINE

压缩 CLI 输出以降低 LLM token 消耗的代理

# TLDR

为 Claude Code / Copilot **安装钩子**（全局）

```rtk init -g```

为 Gemini CLI **安装钩子**

```rtk init -g --gemini```

**运行精简版的 git status**

```rtk git status```

**面向 token 优化的目录列表**

```rtk ls .```

**智能读取源文件**

```rtk read [file.rs]```

**显示 token 节省统计**

```rtk gain```

# SYNOPSIS

**rtk** [*command*|*wrapper*] [*args*...]

# DESCRIPTION

**rtk**（Rust Token Killer）是一个高性能的 CLI 代理，会在命令输出进入 LLM 智能体上下文之前对其进行过滤与压缩。单个 Rust 二进制文件就能支持 100 多个常用开发命令（git、ls、cat/read、grep/rg、测试运行器、docker、linter 等），并运用智能过滤、分组、截断和去重等策略。

**rtk init** 会为各类智能体（Claude Code、Gemini CLI、Codex、Cursor、Windsurf 等）安装钩子或插件，让 Bash 工具调用被自动改写为 **rtk …** 形式。你也可以直接调用这些封装命令（**rtk git status**、**rtk read**、**rtk grep**、**rtk find**、**rtk ls** 等）。

# PARAMETERS

**init** [**-g**] [**--gemini**|**--codex**|**--agent** *name*]

> 安装智能体集成（加 **-g** 为全局安装）。

**gain**

> 显示预估的 token 节省统计。

**git** *git-args...*

> 压缩输出的 git 操作（**status**、**diff**、**log** 等）。

**ls** / **read** / **grep** / **find** / **smart**

> 采用面向 token 格式的文件系统辅助命令（**read -l aggressive** 只输出函数签名）。

其余封装命令覆盖了语言工具链和云 CLI——运行 **rtk --help** 可查看当前完整列表。

# CAVEATS

名称冲突：crates.io 上可能存在一个互不相关的 **rtk** 软件包；如果 **rtk gain** 无法运行，请改用 GitHub 安装脚本或 **cargo install --git** 重新安装。钩子只改写 shell/Bash 工具路径——部分 IDE 原生工具会绕过它们。过滤过于激进可能隐藏模型所需的细节；调试时请直接使用原生命令。

# INSTALL

```brew: brew install rtk```

```nix: nix profile install nixpkgs#rtk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [rg](/man/rg)(1), [gemini](/man/gemini)(1)

# RESOURCES

```[Source code](https://github.com/rtk-ai/rtk)```

```[Homepage](https://www.rtk-ai.app)```

<!-- verified: 2026-07-19 -->
