# TAGLINE

Linux 输入法框架

# TLDR

**启动 IBus 守护进程**

```ibus-daemon -drx```

**列出可用的输入引擎**

```ibus list-engine```

**显示当前输入引擎**

```ibus engine```

**设置当前输入引擎**

```ibus engine [engine_name]```

**重启 IBus 守护进程**

```ibus restart```

**显示 IBus 版本**

```ibus version```

**打印当前配置**

```ibus read-config```

# SYNOPSIS

**ibus** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的 IBus 子命令。

**list-engine**
> 显示可用的输入引擎。

**engine** [_ENGINE_NAME_]
> 显示当前引擎，或将引擎设置为 ENGINE_NAME。

**start**
> 启动 IBus 守护进程。

**restart**
> 重启 IBus 守护进程。

**exit**
> 退出 IBus 守护进程。

**version**
> 显示 IBus 版本。

**read-config**
> 打印配置值。

**reset-config**
> 将配置重置为默认值。

**read-cache**
> 显示注册表缓存。

**write-cache**
> 保存注册表缓存。

**emoji**
> 启动 IBus Emojier。

**help**
> 显示命令列表。

# DESCRIPTION

**IBus**（Intelligent Input Bus）是 Linux 的输入法框架。它支持输入需要复杂输入方式的语言，如中日韩文字。

该框架管理输入法引擎并提供统一接口。它支持多种语言和输入系统。

# CAVEATS

需要桌面环境集成。需要选择输入引擎。X11/Wayland 支持程度不一。

# HISTORY

IBus 由 **Peng Huang** 创建，是 Linux 的新一代输入框架，取代了 SCIM。

# INSTALL

```apt: sudo apt install ibus```

```dnf: sudo dnf install ibus```

```pacman: sudo pacman -S ibus```

```apk: sudo apk add ibus```

```zypper: sudo zypper install ibus```

```nix: nix profile install nixpkgs#ibus```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fcitx](/man/fcitx)(1), [fcitx5](/man/fcitx5)(1)
