# TAGLINE

用于查询 KScreen 显示配置的命令行工具

# TLDR

显示**输出信息**

```kscreen-console outputs```

显示**配置文件路径**

```kscreen-console config```

以 **JSON** 输出配置

```kscreen-console json```

**监视**显示变化

```kscreen-console monitor```

生成**错误报告**数据

```kscreen-console bug```

显示**帮助**

```kscreen-console --help```

# SYNOPSIS

**kscreen-console** [_command_] [_options_]

# DESCRIPTION

**kscreen-console** 是一个命令行工具，用于查询 KDE Plasma 上 KScreen 的显示配置。它提供关于已连接输出、配置文件和显示变化的诊断信息。它通过 DBus 与正在运行的 KScreen 服务通信。

# PARAMETERS

**outputs**
> 显示 KScreen 的输出信息和配置。

**config**
> 显示 KScreen 配置文件的路径。

**json**
> 以 JSON 格式显示当前配置。

**monitor**
> 监视显示配置的变化。

**bug**
> 生成适合错误报告的输出。

**-v**, **--version**
> 显示版本信息。

**--help-all**
> 显示包括 Qt 特有选项在内的帮助。

**-h**, **--help**
> 显示帮助信息。

# CAVEATS

需要启用了 KScreen 的活动 KDE Plasma 会话。通过 DBus 与正在运行的 KScreen 服务通信。

# INSTALL

```apt: sudo apt install kscreen```

```dnf: sudo dnf install kscreen```

```pacman: sudo pacman -S kscreen```

```apk: sudo apk add kscreen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kscreen-doctor](/man/kscreen-doctor)(1), [xrandr](/man/xrandr)(1)
