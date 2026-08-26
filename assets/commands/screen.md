# TAGLINE

支持会话持久化的终端复用器

# TLDR

**启动新的 screen 会话**

```screen```

**启动命名会话**

```screen -S [session_name]```

**列出活动会话**

```screen -ls```

**重新连接到会话**

```screen -r [session_name]```

**脱离当前会话**（在 screen 内部）

```Ctrl+a d```

**创建新窗口**（在 screen 内部）

```Ctrl+a c```

**在窗口间切换**（在 screen 内部）

```Ctrl+a n```（下一个）或 ```Ctrl+a p```（上一个）

**水平分屏**

```Ctrl+a S```

**关闭当前窗口**

```Ctrl+a k```

# SYNOPSIS

**screen** [**-S** _name_] [**-r** [_name_]] [**-ls**] [**-d**] [_command_]

# PARAMETERS

**-S** _name_
> 创建指定名称的会话

**-r** [_name_]
> 重新连接到已脱离的会话

**-R**
> 尽量重新连接，否则启动新会话

**-d**
> 脱离正在运行的会话

**-D**
> 脱离并注销

**-ls**, **-list**
> 列出所有会话

**-x**
> 连接到已被连接的会话（多显示模式）

**-dm**
> 以脱离模式启动（用于脚本）

**-X** _command_
> 向正在运行的会话发送命令

**-L**
> 启用日志记录

**-h** _lines_
> 设置回滚缓冲区大小

# KEY BINDINGS

所有命令以 **Ctrl+a**（命令字符）为前缀：

**Ctrl+a c**: 创建新窗口
**Ctrl+a n/p**: 下一个/上一个窗口
**Ctrl+a "**: 列出窗口
**Ctrl+a 0-9**: 切换到指定编号的窗口
**Ctrl+a d**: 脱离会话
**Ctrl+a k**: 关闭当前窗口
**Ctrl+a S**: 水平分割
**Ctrl+a |**: 垂直分割
**Ctrl+a Tab**: 在区域间切换
**Ctrl+a X**: 关闭当前区域
**Ctrl+a [**: 进入复制/回滚模式
**Ctrl+a ]**: 粘贴
**Ctrl+a ?**: 显示按键绑定

# DESCRIPTION

**screen** 是一款终端复用器，允许在单个窗口中运行多个终端会话。会话可以脱离并重新连接，因此在断开连接后依然保持运行——这对远程工作和长时间运行的进程至关重要。

每个 screen 会话可以包含多个窗口，每个窗口运行自己的 shell 或程序。窗口还可以分割为多个区域，以便同时查看多个窗口。

无论你是主动断开还是因网络问题掉线，会话都会持续存在。这使得 screen 成为在远程服务器上运行进程的必备工具，即使连接中断进程也能存活。

复制模式允许滚动查看终端历史，并在窗口之间或向剪贴板复制文本。

# CONFIGURATION

**~/.screenrc**
> 每用户配置文件，用于设置默认选项、按键绑定、启动窗口和视觉设置。

**/etc/screenrc**
> 系统级配置文件，在每用户配置之前应用于所有用户。

**SCREENDIR**
> 环境变量，覆盖会话套接字的默认目录（默认：/tmp/screens/S-username）。

# CAVEATS

Screen 的默认配置可能与某些终端特性冲突。可通过 **~/.screenrc** 自定义。

命令前缀 **Ctrl+a** 与 readline 的行首快捷键冲突。如有需要可在 .screenrc 中用 **escape** 重新映射。

嵌套的 screen 会话需要按两次前缀（**Ctrl+a a**）才能向内层会话发送命令。

如需功能更丰富的现代替代品，可以考虑 **tmux**。

# HISTORY

Screen 由 **Oliver Laumann** 于 **1987 年**编写，此后由 GNU 项目维护。它是最早的终端复用器之一，奠定了 tmux 等后来者所遵循的范式。

# INSTALL

```apt: sudo apt install screen```

```dnf: sudo dnf install screen```

```pacman: sudo pacman -S screen```

```apk: sudo apk add screen```

```zypper: sudo zypper install screen```

```brew: brew install screen```

```nix: nix profile install nixpkgs#screen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [byobu](/man/byobu)(1), [dtach](/man/dtach)(1), [nohup](/man/nohup)(1)
