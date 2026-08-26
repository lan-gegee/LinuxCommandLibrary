# TAGLINE

在守护进程之外运行 WirePlumber Lua 脚本

# TLDR

**运行 Lua 脚本**

```wpexec [path/to/script.lua]```

**带参数运行脚本**

```wpexec [path/to/script.lua] [arg1] [arg2]```

**显示帮助**

```wpexec --help```

# SYNOPSIS

**wpexec** [_OPTIONS_] _SCRIPT_ [_ARGUMENTS_]

# PARAMETERS

_SCRIPT_
> 要针对正在运行的 WirePlumber 守护进程执行的 Lua 脚本路径。

_ARGUMENTS_
> 传给脚本的位置参数，可通过 **arg** Lua 表访问。

**-h**, **--help**
> 显示帮助信息并退出。

# DESCRIPTION

**wpexec** 在隔离上下文中加载并运行单个 WirePlumber Lua 脚本。与位于 **/usr/share/wireplumber/scripts/** 目录树中、由守护进程管理的脚本不同，**wpexec** 会自行建立到正在运行的 WirePlumber 会话的连接，执行脚本，并在脚本结束后退出。

完整的 WirePlumber Lua API 均可使用，包括 **wp.Core**、**wp.ObjectManager**、**wp.Node** 和 **wp.Link** 等类，因此该工具非常适合临时性的 PipeWire 查询、一次性的图结构操作，以及测试之后可能升级为受管脚本的代码片段。

# CAVEATS

需要 **WirePlumber** 和 **PipeWire** 同时处于运行状态。脚本必须针对系统上安装的 WirePlumber Lua API 版本编写；API 变更记录在 WirePlumber 的发行说明中。脚本内部抛出的错误会传播为 **wpexec** 的退出状态，但一般不会影响长期运行的 WirePlumber 守护进程。

# HISTORY

**wpexec** 随 **WirePlumber** 一起发布。WirePlumber 是在 FreeDesktop.org 框架下开发的 PipeWire 会话与策略管理器。它与 **wpctl** 控制工具并存，让高级用户和打包者可以通过 Lua 驱动 PipeWire，而无需修改守护进程自身的配置。

# INSTALL

```apt: sudo apt install wireplumber```

```dnf: sudo dnf install wireplumber```

```pacman: sudo pacman -S wireplumber```

```apk: sudo apk add wireplumber```

```zypper: sudo zypper install wireplumber```

```brew: brew install wireplumber```

```nix: nix profile install nixpkgs#wireplumber```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wpctl](/man/wpctl)(1), [wireplumber](/man/wireplumber)(1), [pw-cli](/man/pw-cli)(1), [pw-dump](/man/pw-dump)(1)
