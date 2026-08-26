# TAGLINE

自动错误报告的命令行界面

# TLDR

**列出所有检测到的问题**

```abrt-cli list```

**仅列出未上报的问题**

```abrt-cli list -n```

**显示某个问题的详细信息**

```abrt-cli info [problem_dir]```

**将问题上报到已配置的错误跟踪器**

```abrt-cli report [problem_dir]```

**删除一条崩溃报告**

```abrt-cli remove [problem_dir]```

**显示检测到的问题数量**

```abrt-cli status```

**启用或禁用自动上报**

```abrt-cli auto-report [on|off]```

# SYNOPSIS

**abrt-cli** _command_ [_options_] [_problem_dir_]

# DESCRIPTION

**abrt-cli** 是 Automatic Bug Reporting Tool（ABRT，自动错误报告工具）的命令行界面，用于 Fedora 和 RHEL 系统。它管理检测到的应用程序崩溃、内核 oops 以及其他软件缺陷，让用户能够列出、检查、上报和删除问题数据。

崩溃信息包括标识符、时间戳、软件包名称、崩溃原因，以及适用时的上报状态和 URL。

# PARAMETERS

**list** [**-n**] [**--detailed**] [**--since** _NUM_] [**--until** _NUM_]
> 显示检测到的崩溃。**-n** 仅显示未上报的问题。**--detailed** 显示完整报告。**--since**/**--until** 按时间戳过滤。

**info** [**-d**] [**-s** _SIZE_] _PROBLEM_DIR_
> 显示某个问题的详细信息。**-d** 表示详细输出。**-s** 截断超过 SIZE 字节的文本。

**report** [**--delete**] [**--unsafe**] _PROBLEM_DIR_
> 提交问题进行分析和上报。**--delete** 在上报后删除问题目录。**--unsafe** 忽略安全检查。

**remove** _PROBLEM_DIR_
> 从系统中删除一个问题。

**status** [**-b**] [**--since** _NUM_]
> 显示检测到的问题数量。**-b** 仅输出数量（bare 模式）。

**process** [**--since** _NUM_] [**--unsafe**] _PROBLEM_DIR_
> 批量分析并上报问题。

**auto-report** [**on**|**off**]
> 启用或禁用对检测到的问题的自动上报。

**-v**, **--verbose**
> 提高输出的详细程度。

**-V**, **--version**
> 显示版本信息。

# CAVEATS

上报流程会打开一个文本编辑器。编辑器的选择按以下环境变量顺序确定：**$ABRT_EDITOR**、**$VISUAL**、**$EDITOR**，若均未设置则默认为 **vi**。ABRT 守护进程必须处于运行状态才能检测到新问题。

# HISTORY

属于 **ABRT**（Automatic Bug Reporting Tool，自动错误报告工具），由 **Red Hat** 自 **2009** 年前后开始为 Fedora 系系统开发，用于替代 bug-buddy。

# INSTALL

```dnf: sudo dnf install abrt-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[abrt](/man/abrt)(1), [abrt-action-analyze-backtrace](/man/abrt-action-analyze-backtrace)(1), [abrt-action-analyze-c](/man/abrt-action-analyze-c)(1), [coredumpctl](/man/coredumpctl)(1), [journalctl](/man/journalctl)(1)
