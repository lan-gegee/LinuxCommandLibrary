# TAGLINE

将调试过程转化为有证据支撑的 Markdown 报告

# TLDR

在当前项目中**初始化** debugbrief

```debugbrief init```

**开始**新的调试会话

```debugbrief start "[Login returns 500]"```

**运行命令**并将其输出记录为证据

```debugbrief run -- [pytest tests/test_login.py]```

会话期间**添加笔记**

```debugbrief note "[suspect the auth middleware]"```

**重新运行**最近捕获的命令

```debugbrief redo```

**结束**会话并生成报告

```debugbrief end --mode [pr]```

# SYNOPSIS

**debugbrief** _command_ [_arguments_]

# DESCRIPTION

**debugbrief** 记录你调试过程中的操作，并将其转化为适合放进 pull request、工作交接或事故记录的有证据支撑的 Markdown 报告。与 AI 总结工具不同，报告完全由记录到的证据构成：你运行的命令、命令输出、发生变更的文件以及添加的笔记。

典型工作流是：每个项目先执行一次 **init**，然后 **start** 开启会话，**run** 执行并捕获命令，**note** 随手记录观察，最后 **end** 生成报告。生成的文档包括测试结果与文件变更摘要、带耗时的从报错到正常的分析、命令时间线、错误观察以及尝试过的修复方案。报告可以按 **pr**、**handoff** 或 **incident** 三种风格渲染。

debugbrief 是 Python 工具，通常用 **pipx install debugbrief** 安装（也可通过 **uv tool install debugbrief** 或 **pip install debugbrief** 安装）。

# COMMANDS

**init**
> 配置项目并展示工作流。

**start**  _title_
> 以给定标题开始新的调试会话。

**note**  _text_
> 在活动会话中记录一条观察。

**run** **--** _command_
> 执行命令并将其输出捕获为证据。

**redo**
> 重新执行最近捕获的命令。

**end** [**--mode** _pr_|_handoff_|_incident_]
> 生成并保存报告，然后关闭会话。

**status**
> 显示活动会话详情。

**preview** [**--mode** _..._]
> 显示报告但不关闭会话。

**cancel** [**--yes**]
> 放弃活动会话。

**doctor** [**--fix**]
> 校验项目健康状况，可选择修复。

**recover**
> 修复损坏的会话指针。

**last**
> 定位最近的报告。

**open**
> 显示最近的报告。

**list**
> 枚举已记录的会话。

**show**  _id_
> 显示特定的已记录会话。

# CAVEATS

报告只反映通过 debugbrief 捕获的内容；在 **debugbrief run** 之外执行的命令不会作为证据收录。由于输出是逐字存储的，分享报告前请检查其中是否包含机密或敏感数据。

# SEE ALSO

[script](/man/script)(1), [asciinema](/man/asciinema)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/harihkk/Debug-Brief)```

<!-- verified: 2026-06-22 -->
