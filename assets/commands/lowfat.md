# TAGLINE

过滤 CLI 输出，减少噪音和 LLM token 消耗

# TLDR

让命令经过 lowfat 的默认过滤管道**执行**

```lowfat git status```

**显示**某条命令当前生效的过滤器与压缩级别

```lowfat info git```

**显示**累计节省的 token 数量

```lowfat stats```

**设置**全局压缩级别

```lowfat level ultra```

以指定级别为单次命令添加前缀

```LOWFAT_LEVEL=lite lowfat git log```

**安装** OpenCode 插件

```lowfat opencode install```

# SYNOPSIS

**lowfat** [_options_] _command_ [_args_...]

**lowfat** **info** [_command_] [_options_]

**lowfat** **stats** [_options_]

**lowfat** **history**

**lowfat** **level** _lite_|_balanced_|_ultra_

**lowfat** **hook**

**lowfat** **shell-init** _zsh_|_bash_

**lowfat** **plugin** **new** _name_

**lowfat** **plugin** **doctor**

**lowfat** **filter** [_options_]

# PARAMETERS

**--config**
> 打印完整的最终生效配置。

**--explain**
> 显示哪些过滤器被运行及其原因（配合 **filter** 使用）。

**--audit**
> 在 **stats** 中包含最近的插件执行详情。

**--sub** _name_
> 选择插件的子管道（配合 **filter** 使用）。

**--level** _level_
> 为单次调用覆盖压缩级别（**lite**、**balanced**、**ultra**）。

# DESCRIPTION

**lowfat** 是一个轻量的 Rust CLI，位于 Shell 命令之前，在输到达人类读者或 AI 编程智能体之前剔除冗余输出。它针对的常见场景是：**git**、**docker**、**ls** 等工具输出大量冗长文本，既浪费上下文窗口空间又不提供决策价值。

该工具以单个二进制文件发布，内置多种处理器并提供插件系统。插件是存放于 **~/.lowfat/plugins/** 下的 **.lf** 过滤脚本；**lowfat plugin new** 可生成新插件脚手架，**lowfat plugin doctor** 用于校验已安装的插件。

集成方式包括：直接加前缀（**lowfat docker ps**）、通过 **eval "$(lowfat shell-init zsh)"** 注入 Shell 钩子（当设置 **CLAUDECODE=1**、**CODEX_ENV** 或 **LOWFAT_ENABLE=1** 时自动激活）、Claude Code 的 **PreToolUse** 钩子（**lowfat hook**），以及 OpenCode 插件（**lowfat opencode install**）。**lowfat history** 会按潜在节省空间对各命令排序，方便你针对自己的工作流调优过滤器。

压缩级别（**lite**、**balanced**、**ultra**）决定输出裁剪的激进程度。配置存放在 **~/.lowfat**，可用 **LOWFAT_LEVEL** 或 **--level** 按次覆盖。

# CONFIGURATION

**~/.lowfat/**
> 用户配置目录，存放管道定义和插件。

**LOWFAT_LEVEL**
> 强制单条命令使用指定压缩级别的环境变量。

**LOWFAT_ENABLE=1**
> 即使不在智能体环境中也强制启用 Shell 集成。

# CAVEATS

**lowfat** 通过删除细节来减少 token；调试时请用 **lowfat info** 核查关键输出，或去掉前缀直接运行底层命令。Shell 集成会透明地改写命令，可能让忘记其处于启用状态的用户感到意外。基于 Python 的插件可能需要 **uv** 来解析依赖（**lowfat plugin doctor** 会检查这一点）。

# INSTALL

```aur: yay -S lowfat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [docker](/man/docker)(1), [awk](/man/awk)(1)
