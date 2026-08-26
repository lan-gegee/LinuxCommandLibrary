# TAGLINE

面向具备计算机操作能力的 AI 编程代理的沙箱启动器

# TLDR

在沙箱中**运行默认代理**

```cuabot```

**启动指定代理**（claude、codex、aider、openclaw、gemini、vibe）

```cuabot [agent]```

在沙箱中**运行任意命令**

```cuabot [command]```

**启动一个具名的隔离**会话

```cuabot -n [session_name] [agent]```

对沙箱**截图**

```cuabot --screenshot [path/to/output.png]```

在指定坐标处**点击**

```cuabot --click [x] [y]```

在沙箱内**运行 bash 命令**

```cuabot --bash "[command]"```

**启动后台守护进程**

```cuabot --serve [port]```

检查守护进程状态

```cuabot --status```

# SYNOPSIS

**cuabot** [_options_] [_agent_ | _command_]

# DESCRIPTION

**cuabot** 是一个 TUI 启动器，可将任意 CLI 编程代理（Claude Code、Codex、Aider、OpenClaw 等）或 GUI 应用运行在具备计算机操作能力的隔离沙箱中。每个代理拥有自己的窗口，该窗口被串流到宿主桌面，并支持剪贴板共享和音频，同时与宿主系统保持隔离。

沙箱暴露了 computer-use API，使代理能够在容器内截图、点击、输入、滚动和运行 Shell 命令。使用 **-n** 可并发运行多个隔离会话，每个会话都有独立的容器和端口。

# COMMANDS

**cuabot** _agent_
> 在沙箱中启动指定名称的代理（如 _claude_、_codex_、_aider_、_openclaw_、_gemini_、_vibe_）。

**cuabot** _command_
> 在沙箱内执行任意命令。

**--serve** [_port_]
> 在可选端口上启动 **cuabotd** 守护进程。

**--stop**
> 停止正在运行的守护进程。

**--status**
> 打印守护进程状态。

# COMPUTER-USE OPTIONS

**--screenshot** [_path_]
> 捕获沙箱显示画面的截图。

**--click** _x_ _y_ [_button_]
> 在给定坐标处点击，可选指定按键。

**--doubleclick** _x_ _y_
> 在给定坐标处双击。

**--move** _x_ _y_
> 将鼠标移动到坐标处。

**--mousedown** / **--mouseup** _x_ _y_
> 按下或释放鼠标按键。

**--drag** _x1_ _y1_ _x2_ _y2_
> 从一个坐标拖拽到另一个坐标。

**--scroll** _x_ _y_ _dx_ _dy_
> 在指定位置按给定的增量滚动。

**--type** _text_
> 输入指定的字符串。

**--key** _key_
> 按下并释放单个按键。

**--keydown** _key_ / **--keyup** _key_
> 只按下不释放，或只释放不按下某个按键。

**--bash** _command_
> 在沙箱内运行 bash 命令。

# OPTIONS

**-n**, **--name** _name_
> 使用具名的隔离会话（独立的容器和端口）。

**--help**
> 显示用法信息。

# CAVEATS

沙箱是为可能执行任意命令的 AI 代理设计的。虽然容器化将代理与宿主隔离开，但把剪贴板、麦克风或敏感凭证共享进沙箱可能导致数据泄露。应将沙箱边界视为纵深防御的一环，而不是替代对代理行为的代码审查。

# HISTORY

**cuabot** 由 **trycua** 开发，是 **Cua** 项目的一部分——这是一个面向**计算机操作代理（Computer-Use Agents）**的开源平台。该工具旨在提供统一的沙箱层，让任何编程代理都能接入，从而将代理与宿主环境解耦。

# SEE ALSO

[claude](/man/claude)(1), [aider](/man/aider)(1), [docker](/man/docker)(1), [chromium](/man/chromium)(1)
