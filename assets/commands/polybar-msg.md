# TAGLINE

向运行中的 Polybar 发送 IPC 消息

# TLDR

**向模块发送操作**

```polybar-msg action [module] [action]```

**切换模块可见性**

```polybar-msg action [module] toggle```

**向 IPC 模块发送钩子**

```polybar-msg hook [module] [hook_index]```

**退出 polybar**

```polybar-msg cmd quit```

# SYNOPSIS

**polybar-msg** [_options_] _command_ [_args_...]

# PARAMETERS

**action** _module_ _action_
> 向模块发送操作。

**hook** _module_ _index_
> 触发 IPC 钩子。

**cmd** _command_
> 发送命令（quit、restart、hide、show、toggle）。

**-p** _pid_
> 定位特定的 polybar PID。

# DESCRIPTION

**polybar-msg** 向运行中的 polybar 实例发送 IPC 消息。它可以控制模块、触发钩子并管理 polybar 的生命周期，适用于动态更新状态栏以及脚本化交互。

# INSTALL

```apt: sudo apt install polybar```

```dnf: sudo dnf install polybar```

```pacman: sudo pacman -S polybar```

```apk: sudo apk add polybar```

```zypper: sudo zypper install polybar```

```nix: nix profile install nixpkgs#polybar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[polybar](/man/polybar)(1)
