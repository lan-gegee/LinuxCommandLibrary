# TAGLINE

可编程、兼容 tmux 的终端复用器

# TLDR

**创建一个新的分离会话**，名为 **ci**

```rmux new-session -d -s [ci]```

**向会话发送命令**，就像手动键入一样

```rmux send-keys -t [ci] "[printf 'ok\n']" Enter```

**捕获当前窗格**的输出

```rmux capture-pane -p -t [ci]```

**连接**到已有会话

```rmux attach -t [ci]```

**列出**所有会话

```rmux list-sessions```

**等待**指定信号触发

```rmux wait-for [ci-done]```

**终止**一个会话

```rmux kill-session -t [ci]```

# SYNOPSIS

**rmux** _command_ [_command-options_]

**rmux** [**-t** _target_] [**-s** _name_] [**-d**] ...

# PARAMETERS

**new-session**, **new**
> 创建会话。**-d** 使其分离；**-s** _NAME_ 为其命名；**-c** _DIR_ 设置工作目录。

**attach-session**, **attach**
> 将当前终端连接到 **-t** _TARGET_ 指定的已有会话。

**list-sessions**, **ls**
> 打印所有已知会话及其 ID 和状态。

**send-keys**
> 向目标窗格发送按键或字面文本。特殊按键（**Enter**、**C-c**、**Escape**、**Up** 等）作为独立参数识别。

**capture-pane**
> 转储窗格的可见缓冲区。**-p** 打印到 stdout；**-S** _LINE_ / **-E** _LINE_ 选择历史范围。

**wait-for**
> 阻塞直到通过 **rmux wait-for -S** _NAME_ 触发指定信号。

**kill-session**, **kill-server**
> 终止一个会话或整个服务器。

**-t** _TARGET_
> 目标窗格或会话（例如 **ci**、**ci:0.1**）。

**-s** _NAME_
> 创建时的会话名称。

**-d**
> 分离（不把终端连接到新会话）。

**-c** _DIR_
> 为新会话或窗口设置工作目录。

# DESCRIPTION

**rmux** 是一个用 Rust 实现的终端复用器，具有与 tmux 兼容的命令接口（实现了全部 90 个命令），以及用于从代码驱动会话的类型化 SDK。它面向智能体自动化、无头 CI 工作流和交互式使用，可在 Linux、macOS 和 Windows 上原生运行（包括使用 Windows 命名管道作为本地传输方式）。

会话是持久的：在会话内启动的进程在控制终端断开后会继续运行，之后可以重新连接、检查或继续驱动。每个会话都是由窗口和窗格构成的树，可通过名称或 ID 寻址，与 tmux 语义保持一致，因此现有的 tmux 配置和操作习惯大多可以直接沿用。

除了经典的复用功能之外，**rmux** 还提供结构化快照和终端原生的定位器，让 SDK 或 CLI 使用者可以把 TUI 当作可寻址的界面来处理——发送按键并读回屏幕的稳定表示。这使它可以作为 AI 智能体或测试框架的后端引擎，以确定性的方式驱动交互式程序。

# CAVEATS

虽然命令接口力求与 tmux 对齐，但边界行为和配置语义可能存在差异；不会解析已有的 **.tmux.conf** 文件。该项目尚年轻（2026 年中的 v0.2.0）；API 和磁盘上的会话格式仍可能变化。会话仅存在于 **rmux** 服务器进程中，服务器被杀死后即丢失。

# HISTORY

**rmux** 由 **Helvesec** 开发（**github.com/helvesec/rmux**），v0.2.0 发布于 **2026 年 5 月 18 日**。它通过 shell 脚本（macOS/Linux）、PowerShell 安装程序（Windows）以及 Cargo crate 分发跨平台二进制文件，并同时提供类型化的 Rust SDK。

# INSTALL

```brew: brew install rmux```

```nix: nix profile install nixpkgs#rmux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [zellij](/man/zellij)(1), [abduco](/man/abduco)(1)
