# TAGLINE

向 Sway 合成器发送 IPC 命令

# TLDR

**发送命令**

```swaymsg [command]```

**获取工作区**

```swaymsg -t get_workspaces```

**获取输出**

```swaymsg -t get_outputs```

**获取焦点窗口**

```swaymsg -t get_tree | jq '.. | select(.focused?)'```

**重新加载配置**

```swaymsg reload```

**退出 sway**

```swaymsg exit```

**移动工作区**

```swaymsg move workspace to output [HDMI-A-1]```

# SYNOPSIS

**swaymsg** [_-t type_] [_-m_] [_options_] _message_

# PARAMETERS

**-t**, **--type** _TYPE_
> 消息类型。

**-m**, **--monitor**
> 持续监听响应直到被终止。只能与 subscribe 消息类型配合使用。

**-p**, **--pretty**
> 即使未连接 tty 也使用美观输出。

**-r**, **--raw**
> 即使连接了 tty 也使用原始 JSON 输出。

**-q**, **--quiet**
> 发送 IPC 消息但不打印响应。

**-s**, **--socket** _PATH_
> 使用指定的套接字路径而不是 SWAYSOCK 环境变量。

# MESSAGE TYPES

**get_workspaces** - 列出工作区及其状态
**get_outputs** - 列出输出及其属性
**get_tree** - 所有窗口、容器、输出和工作区的 JSON 编码布局树
**get_marks** - 窗口标记列表
**get_bar_config** - 栏配置
**get_version** - Sway 版本信息
**get_inputs** - 当前输入设备列表
**get_seats** - seat 及其分配设备的列表
**get_binding_modes** - 已配置绑定模式的列表
**subscribe** - 订阅事件类型（配合 -m 使用）

# DESCRIPTION

**swaymsg** 是 Sway Wayland 合成器的 IPC（进程间通信）客户端。它通过 IPC 套接字向正在运行的 Sway 实例发送命令和查询，实现窗口管理操作（移动、调整大小、聚焦等）的脚本化控制。

查询类消息类型（get_workspaces、get_outputs、get_tree）返回描述当前合成器状态的 JSON 数据，可用 jq 之类的工具解析。这使 swaymsg 非常适合构建自定义状态栏、自动化脚本和工作区管理工具。

监听模式订阅 Sway 事件并实时打印，便于调试和编写响应式脚本。IPC 套接字路径默认取自 Sway 设置的 SWAYSOCK 环境变量。

# CAVEATS

必须先启动 Sway。需要套接字权限。JSON 输出需要解析。

# HISTORY

**swaymsg** 是 **Sway** 合成器的 IPC 客户端，在 Wayland 上对应 i3-msg 的功能。

# INSTALL

```apt: sudo apt install sway```

```dnf: sudo dnf install sway```

```pacman: sudo pacman -S sway```

```apk: sudo apk add sway```

```zypper: sudo zypper install sway```

```nix: nix profile install nixpkgs#sway```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sway](/man/sway)(1), [jq](/man/jq)(1), [i3-msg](/man/i3-msg)(1)
