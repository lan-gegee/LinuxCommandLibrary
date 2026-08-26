# TAGLINE

Hyprland（动态平铺 Wayland 合成器）的命令行控制工具

# TLDR

**重载** Hyprland 配置

```hyprctl reload```

返回**活动窗口**名称

```hyprctl activewindow```

列出所有已连接的**输入设备**

```hyprctl devices```

列出所有**工作区**及其属性

```hyprctl workspaces```

调用一个 **dispatcher**

```hyprctl dispatch [dispatcher]```

动态设置**配置关键字**

```hyprctl keyword [keyword] [value]```

显示**版本**

```hyprctl version```

# SYNOPSIS

**hyprctl** [_command_] [_arguments_]

# PARAMETERS

**reload**
> 重载 Hyprland 配置

**activewindow**
> 显示活动窗口信息

**devices**
> 列出输入设备

**workspaces**
> 列出工作区

**monitors**
> 列出显示器及其属性

**clients**
> 列出所有窗口/客户端

**dispatch** _DISPATCHER_ [_ARGS_]
> 执行一个 dispatcher（窗口操作、工作区切换）

**keyword** _KEY_ _VALUE_
> 在运行时设置配置选项

**setcursor** _THEME_ _SIZE_
> 设置光标主题和大小

**switchxkblayout** _DEVICE_ _CMD_
> 切换键盘布局（_CMD_ 为 `next`、`prev` 或布局索引）

**getoption** _SECTION.OPTION_
> 打印配置选项的当前值，例如 `getoption general.border_size`

**layers**
> 列出 layer-shell 表面（状态栏、启动器、通知等）

**notify** _ICON_ _TIME_MS_ _COLOR_ _MESSAGE_
> 使用 Hyprland 内置的通知系统在屏幕上显示通知

**seterror** _COLOR_ _MESSAGE_ | disable
> 设置（或清除）持久显示的错误栏消息

**eval** _LUA_
> 对 Lua 配置 API 运行 Lua 表达式（例如 `hl.dispatch(...)`），随 Hyprland 可选的 Lua 配置一同引入

**repl**
> 启动交互式 Lua REPL，使用与 **eval** 相同的 API

**output** create|remove _BACKEND_ [_NAME_]
> 添加或移除虚拟输出（`wayland`、`headless` 或 `auto` 后端）

**--batch** _CMD1;CMD2;..._
> 在一次请求中执行多条命令，以分号分隔——相比多次单独调用可减少 IPC 往返

**-j**
> 以 JSON 格式输出

**-r**
> 在发出命令后强制刷新状态（例如布局或规则变化之后）

**-i** _INSTANCE_
> 当有多个实例运行时，指定目标 Hyprland 实例（来自 `hyprctl instances` 的 id 或索引）

# DESCRIPTION

**hyprctl** 是动态平铺 Wayland 合成器 Hyprland 的命令行控制工具。它通过合成器的 IPC 套接字与运行中的合成器通信，查询状态（显示器、工作区、客户端、设备）并在运行时触发操作；它会随 Hyprland 自动安装。

Dispatcher 控制移动窗口、切换工作区、执行程序等操作，通过 `hyprctl dispatch <DISPATCHER> [ARGS]` 调用。常用的 dispatcher 包括 **exec**、**killactive**、**workspace**、**movewindow**、**fullscreen** 和 **togglefloating**；完整列表见 Hyprland wiki 的 Dispatchers 页面。

运行时配置值可通过 **getoption** 读取，并通过 **keyword** _SECTION.OPTION_ _VALUE_ 设置；这样做的修改会在下次 **reload** 时丢失，除非同时写入配置文件。自 Hyprland 加入可选的基于 Lua 的配置（`hyprland.lua`）后，**hyprctl eval** 和 **hyprctl repl** 暴露了同一套 Lua API（`hl.dispatch`、`hl.config` 等）供脚本使用，而传统的 **keyword**/**dispatch** 接口仍可用于基于 `hyprland.conf` 的配置方式。

由于 hyprctl 调用由合成器同步处理，快速连续发出大量调用（例如来自脚本）可能造成明显的卡顿——请改用 **--batch** 将多条命令打包为单次请求。

# CAVEATS

仅在 Hyprland 运行时有效，且只能通过 `$XDG_RUNTIME_DIR/hypr` 下的 Unix 套接字与本地的 Hyprland 实例通信。通过 **keyword** 所做的修改不会在重启或重载后保留，除非同时保存到配置文件。Lua 配置系统（以及 **eval**/**repl**）是可选的，仅当 `~/.config/hypr/hyprland.lua` 存在时才启用；否则 Hyprland 回退到传统的 `hyprland.conf`。

# HISTORY

hyprctl 是 Hyprland 项目的一部分。Hyprland 由 **Vaxry** 创建的 Wayland 合成器，于 **2022 年**首次发布，以其动画效果、动态平铺和高度可定制性著称。**2026 年**，Hyprland 0.55 加入了可选的 Lua 配置系统，为 hyprctl 扩展了用于脚本的 **eval** 和 **repl** 命令，与既有的 keyword/dispatch 接口并存。

# INSTALL

```pacman: sudo pacman -S hyprland```

```apk: sudo apk add hyprland```

```zypper: sudo zypper install hyprland```

```nix: nix profile install nixpkgs#hyprland```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hyprpaper](/man/hyprpaper)(1), [hyprshot](/man/hyprshot)(1), [swaymsg](/man/swaymsg)(1)

# RESOURCES

```[Source code](https://github.com/hyprwm/Hyprland)```

```[Homepage](https://hyprland.org)```

```[Documentation](https://wiki.hypr.land/Configuring/Advanced-and-Cool/Using-hyprctl/)```

<!-- verified: 2026-07-19 -->
