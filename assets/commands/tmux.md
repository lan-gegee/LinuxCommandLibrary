# TAGLINE

支持会话持久化的终端复用器

# TLDR

**启动新会话**

```tmux```

**启动新的命名会话**

```tmux new -s [session_name]```

**列出会话**

```tmux ls```

**连接到最近使用的会话**

```tmux attach```

**连接到命名会话**

```tmux attach -t [session_name]```

**脱离当前会话**（在 tmux 内部）

```Ctrl-b d```

**终止一个会话**

```tmux kill-session -t [session_name]```

**启动运行命令的分离式会话**

```tmux new -d -s [session_name] '[command]'```

**重新加载配置文件**

```tmux source-file ~/.tmux.conf```

# SYNOPSIS

**tmux** [**-2CDlNuvV**] [**-c** _shell-command_] [**-f** _file_] [**-L** _socket-name_] [**-S** _socket-path_] [_command_ [_flags_]]

# PARAMETERS

**-2**
> 强制 tmux 认为终端支持 256 色。

**-c** _shell-command_
> 使用默认 shell 执行 shell-command，类似 sh -c。

**-f** _file_
> 指定替代的配置文件。

**-L** _socket-name_
> 使用命名的套接字，允许多个独立的服务器并行运行。

**-S** _socket-path_
> 指定服务器套接字的完整路径而不是名称。

**-u**
> 强制 tmux 认为终端支持 UTF-8。

**-V**
> 报告 tmux 版本。

**new-session**, **new** [**-d**] [**-s** _name_]
> 创建新会话；-d 以分离方式启动。

**attach-session**, **attach** [**-t** _target_]
> 连接到已有会话。

**list-sessions**, **ls**
> 列出受管理的会话。

**detach-client**, **detach**
> 将当前客户端从其会话中脱离。

**kill-session** [**-t** _target_]
> 销毁会话并关闭其窗口。

**kill-server**
> 终止 tmux 服务器和所有会话。

**split-window** [**-h**] [**-v**]
> 分割活动窗格；-h 左右分割，-v 上下分割（默认）。

**send-keys** [**-t** _target_] _keys_
> 向窗口或窗格发送按键。

**source-file** _file_
> 执行配置文件中的命令。

**list-keys**, **lsk**
> 列出所有已绑定的按键及其执行的命令。

**resize-pane** [**-UDLR**] [_amount_]
> 在给定方向上调整活动窗格的大小。

**swap-window** [**-s** _src_] [**-t** _dst_]
> 交换两个窗口。

# KEY BINDINGS

所有按键都在前缀 **Ctrl-b** 之后按下：

**?**：列出所有按键绑定
**:**：打开 tmux 命令提示符

**d**：脱离会话
**$**：重命名当前会话
**s**：交互式选择会话
**(** / **)**：切换到上一个/下一个会话

**c**：创建新窗口
**,**：重命名当前窗口
**&**：终止当前窗口（要求确认）
**n** / **p**：下一个/上一个窗口
**0-9**：按编号切换窗口
**l**：切换到最近选择的窗口
**w**：交互式选择窗口

**"**：将窗格上下分割
**%**：将窗格左右分割
**上/下/左/右**：移动到该方向的窗格
**o**：循环切换窗格
**q**：显示窗格编号（按数字选择）
**x**：终止当前窗格（要求确认）
**z**：切换当前窗格的缩放状态
**!**：将当前窗格拆分为独立的新窗口
**{** / **}**：将当前窗格与上一个/下一个窗格交换
**Space**：循环切换预设的窗格布局

**[**：进入复制模式（回滚、搜索、复制文本）
**]**：粘贴最近复制的文本

# DESCRIPTION

**tmux**（terminal multiplexer，终端复用器）让单个终端承载多个会话，每个会话包含多个窗口（类似标签页），窗口还可以分割成窗格。它以客户端-服务器系统方式运行：服务器在后台保持会话存活，客户端可以随时连接和脱离这些会话。

由于会话持久保存在服务器上，工作可以在 SSH 断开或主动脱离后继续存在——重新用 **tmux attach** 连接即可完全恢复原状。这使得 tmux 成为远程服务器管理、长时间运行任务和结对编程（多个客户端可连接同一会话）的必备工具。

在 tmux 内部，前缀键（默认 **Ctrl-b**）加命令键触发操作，命令提示符（前缀 **:**）可按名称执行任何 tmux 命令。行为、按键绑定和状态栏都可以通过配置文件自定义。

# CONFIGURATION

**~/.tmux.conf**, **~/.config/tmux/tmux.conf**
> 用户配置文件，用于按键绑定、状态栏定制、默认选项和插件。在服务器启动时读取；可用 **tmux source-file** 重新加载到运行中的服务器。

**/etc/tmux.conf**
> 系统级配置，先于用户文件应用。

# CAVEATS

默认前缀 **Ctrl-b** 会遮蔽 readline/emacs 的“后退一个字符”绑定；许多用户将其重新绑定为 **Ctrl-a**。回滚查看输出需要先进入复制模式。tmux 在会话内部将 **TERM** 设置为 screen 或 tmux-256color，这可能会让检测特定终端的程序产生混淆。在 tmux 中嵌套 tmux 时，需按两次前缀才能发送给内层会话。配置更改只有在重新加载文件或重启服务器后才会生效。

# HISTORY

**tmux** 由 **Nicholas Marriott** 编写，于 **2007 年**首次发布，是一个代码库更整洁、采用客户端-服务器设计的 BSD 许可 GNU Screen 替代品。它在 **2009 年**（OpenBSD 4.6）成为 OpenBSD 基本系统的一部分，可移植版则为 Linux、macOS 及其他平台打包。该项目仍在活跃开发中。

# INSTALL

```apt: sudo apt install tmux```

```dnf: sudo dnf install tmux```

```pacman: sudo pacman -S tmux```

```apk: sudo apk add tmux```

```zypper: sudo zypper install tmux```

```brew: brew install tmux```

```nix: nix profile install nixpkgs#tmux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[screen](/man/screen)(1), [zellij](/man/zellij)(1), [byobu](/man/byobu)(1), [dtach](/man/dtach)(1), [abduco](/man/abduco)(1), [tmuxinator](/man/tmuxinator)(1)

# RESOURCES

```[Source code](https://github.com/tmux/tmux)```

```[Documentation](https://github.com/tmux/tmux/wiki)```

<!-- verified: 2026-06-12 -->
